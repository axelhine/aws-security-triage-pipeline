
import unittest
from unittest.mock import patch

from threat_intelligence import enrich_ip


class TestCombinedEnrichment(unittest.TestCase):

    @patch("threat_intelligence.lookup_shodan")
    @patch("threat_intelligence.lookup_otx")
    def test_both_sources_success(self, mock_otx, mock_shodan):

        mock_otx.return_value = {
            "status": "success",
            "source": "OTX",
            "pulse_count": 0
        }

        mock_shodan.return_value = {
            "status": "success",
            "source": "Shodan",
            "ports": [443, 53]
        }

        result = enrich_ip("8.8.8.8")

        self.assertEqual(result["status"], "success")
        self.assertEqual(result["otx"]["status"], "success")
        self.assertEqual(result["shodan"]["status"], "success")

        mock_otx.assert_called_once_with("8.8.8.8")
        mock_shodan.assert_called_once_with("8.8.8.8")


    
    @patch("threat_intelligence.lookup_shodan")
    @patch("threat_intelligence.lookup_otx")
    def test_ineligible_ips_skip_lookups(self, mock_otx, mock_shodan):

        test_ips = [
            "192.168.1.1",   # Private IPv4
            "192.0.2.10",    # Documentation IPv4
            "127.0.0.1",     # Loopback IPv4
            "999.999.999.999"  # Invalid IPv4
        ]

        for ip in test_ips:
            with self.subTest(ip=ip):
                result = enrich_ip(ip)

                self.assertEqual(result["status"], "skipped")

        # Neither provider should have been contacted.
        mock_otx.assert_not_called()
        mock_shodan.assert_not_called()


    @patch("threat_intelligence.lookup_shodan")
    @patch("threat_intelligence.lookup_otx")
    def test_partial_provider_failure(self, mock_otx, mock_shodan):
        # Simulate OTX failing to respond.
        mock_otx.return_value = {
            "status": "error",
            "source": "OTX",
            "reason": "Connection timed out"
        }

        # Simulate Shodan responding successfully.
        mock_shodan.return_value = {
            "status": "success",
            "source": "Shodan",
            "ports": [443, 53]
        }

        result = enrich_ip("8.8.8.8")

        # Verify the current coordinator behavior.
        self.assertEqual(result["status"], "partial")
        self.assertEqual(result["otx"]["status"], "error")
        self.assertEqual(result["shodan"]["status"], "success")

        # Verify both providers were called exactly once.
        mock_otx.assert_called_once_with("8.8.8.8")
        mock_shodan.assert_called_once_with("8.8.8.8")

    @patch("threat_intelligence.lookup_shodan")
    @patch("threat_intelligence.lookup_otx")
    def test_both_providers_fail(self, mock_otx, mock_shodan):

        # Simulate both intelligence providers failing.
        mock_otx.return_value = {
            "status": "error",
            "source": "OTX",
            "reason": "Connection timed out"
        }

        mock_shodan.return_value = {
            "status": "error",
            "source": "Shodan",
            "reason": "Service unavailable"
        }

        # Run enrichment without making real API requests.
        result = enrich_ip("8.8.8.8")

        # Neither provider returned usable intelligence.
        self.assertEqual(result["status"], "error")
        self.assertEqual(result["otx"]["status"], "error")
        self.assertEqual(result["shodan"]["status"], "error")

        # Verify both providers were contacted exactly once.
        mock_otx.assert_called_once_with("8.8.8.8")
        mock_shodan.assert_called_once_with("8.8.8.8")


if __name__ == "__main__":
    unittest.main()
