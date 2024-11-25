# coding: utf-8

"""
    CZERTAINLY Core API

    REST API for CZERTAINLY Core

    The version of the OpenAPI document: 2.13.2-SNAPSHOT
    Contact: info@czertainly.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pyCZERTAINLY.api.ra_profile_management_api import RAProfileManagementApi


class TestRAProfileManagementApi(unittest.TestCase):
    """RAProfileManagementApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RAProfileManagementApi()

    def tearDown(self) -> None:
        pass

    def test_activate_acme_for_ra_profile(self) -> None:
        """Test case for activate_acme_for_ra_profile

        Activate ACME for RA Profile
        """
        pass

    def test_activate_cmp_for_ra_profile(self) -> None:
        """Test case for activate_cmp_for_ra_profile

        Activate CMP for RA Profile
        """
        pass

    def test_activate_scep_for_ra_profile(self) -> None:
        """Test case for activate_scep_for_ra_profile

        Activate SCEP for RA Profile
        """
        pass

    def test_associate_ra_profile_with_approval_profile(self) -> None:
        """Test case for associate_ra_profile_with_approval_profile

        Associated RA profile with the Approval profile
        """
        pass

    def test_bulk_delete_ra_profile(self) -> None:
        """Test case for bulk_delete_ra_profile

        Delete multiple RA Profiles
        """
        pass

    def test_bulk_disable_ra_profile(self) -> None:
        """Test case for bulk_disable_ra_profile

        Disable multiple RA Profiles
        """
        pass

    def test_bulk_enable_ra_profile(self) -> None:
        """Test case for bulk_enable_ra_profile

        Enable multiple RA Profiles
        """
        pass

    def test_check_ra_profile_compliance(self) -> None:
        """Test case for check_ra_profile_compliance

        Initiate Certificate Compliance Check
        """
        pass

    def test_create_ra_profile(self) -> None:
        """Test case for create_ra_profile

        Create RA Profile
        """
        pass

    def test_deactivate_acme_for_ra_profile(self) -> None:
        """Test case for deactivate_acme_for_ra_profile

        Deactivate ACME for RA Profile
        """
        pass

    def test_deactivate_cmp_for_ra_profile(self) -> None:
        """Test case for deactivate_cmp_for_ra_profile

        Deactivate CMP for RA Profile
        """
        pass

    def test_deactivate_scep_for_ra_profile(self) -> None:
        """Test case for deactivate_scep_for_ra_profile

        Deactivate SCEP for RA Profile
        """
        pass

    def test_delete_ra_profile(self) -> None:
        """Test case for delete_ra_profile

        Delete RA Profile
        """
        pass

    def test_delete_ra_profile_without_authority(self) -> None:
        """Test case for delete_ra_profile_without_authority

        Delete RA Profile
        """
        pass

    def test_disable_ra_profile(self) -> None:
        """Test case for disable_ra_profile

        Disable RA Profiles
        """
        pass

    def test_disassociate_ra_profile_from_approval_profile(self) -> None:
        """Test case for disassociate_ra_profile_from_approval_profile

        Disassociated RA profile with the Approval profile
        """
        pass

    def test_edit_ra_profile(self) -> None:
        """Test case for edit_ra_profile

        Edit RA Profile
        """
        pass

    def test_enable_ra_profile(self) -> None:
        """Test case for enable_ra_profile

        Enable RA Profiles
        """
        pass

    def test_get_acme_for_ra_profile(self) -> None:
        """Test case for get_acme_for_ra_profile

        Get ACME details for RA Profile
        """
        pass

    def test_get_associated_approval_profiles(self) -> None:
        """Test case for get_associated_approval_profiles

        List of Approval profiles associated with the RAProfile
        """
        pass

    def test_get_associated_compliance_profiles(self) -> None:
        """Test case for get_associated_compliance_profiles

        Get Compliance Profiles for an RA Profile
        """
        pass

    def test_get_authority_certificate_chain(self) -> None:
        """Test case for get_authority_certificate_chain

        Retrieve certificates of authority belonging to RA profile
        """
        pass

    def test_get_cmp_for_ra_profile(self) -> None:
        """Test case for get_cmp_for_ra_profile

        Get CMP details for RA Profile
        """
        pass

    def test_get_ra_profile(self) -> None:
        """Test case for get_ra_profile

        Details of RA Profile
        """
        pass

    def test_get_ra_profile_without_authority(self) -> None:
        """Test case for get_ra_profile_without_authority

        Details of RA Profile
        """
        pass

    def test_get_scep_for_ra_profile(self) -> None:
        """Test case for get_scep_for_ra_profile

        Get SCEP details for RA Profile
        """
        pass

    def test_list_ra_profile_issue_certificate_attributes(self) -> None:
        """Test case for list_ra_profile_issue_certificate_attributes

        Get issue Certificate Attributes
        """
        pass

    def test_list_ra_profile_revoke_certificate_attributes(self) -> None:
        """Test case for list_ra_profile_revoke_certificate_attributes

        Get revocation Attributes
        """
        pass

    def test_list_ra_profiles(self) -> None:
        """Test case for list_ra_profiles

        List of available RA Profiles
        """
        pass


if __name__ == '__main__':
    unittest.main()
