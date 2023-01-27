"""
Tests for dri-preingest-sip-error event.
"""
import unittest
import test_utils
import jsonschema
from tre_event_lib import tre_event_api


event_valid = test_utils.load_test_event(event_file_name="dri-preingest-sip-error.json")

event_invalid_parameter_name = test_utils.load_test_event(
    event_file_name="dri-preingest-sip-error-error.json"
)

EVENT_NAME = "dri-preingest-sip-error"


class TestDriPreingestSipErrorSchema(unittest.TestCase):
    """Tests for dri-preingest-sip-error event."""

    def test_event_valid(self):
        """Test dri-preingest-sip-error schema."""
        tre_event_api.validate_event(event=event_valid)

    def test_invalid_parameter_name(self):
        """Test dri-preingest-sip-error schema fails with invalid event-name."""

        try:
            tre_event_api.validate_event(
                event=event_invalid_parameter_name, schema_name=EVENT_NAME
            )

            self.fail("Did not get expected exception")
        except jsonschema.exceptions.ValidationError as validation_error:
            expected = "'foo' is not one of ['dri-preingest-sip-error']"
            self.assertTrue(expected in str(validation_error))
