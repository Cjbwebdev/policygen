"""
Sprint 4 T1 TDD tests — Fix hardcoded counter.
Tests written BEFORE code changes (RED phase).
Run with: pytest tests/test_sprint4.py -v
"""
import pytest
from django.test import TestCase, Client
from django.urls import reverse
from policies.models import PolicyDocument


class TestHomepageCounterUsesRealData(TestCase):
    """T1: The doc_count on the homepage must come from the real DB — no hardcoded fallback."""

    def setUp(self):
        self.client = Client()
        # Clean slate
        PolicyDocument.objects.all().delete()

    def test_counter_zero_when_no_docs(self):
        """When DB is empty, counter must show 0 — not a fake number."""
        response = self.client.get(reverse('policies:home'))
        self.assertEqual(response.status_code, 200)
        doc_count = response.context.get('doc_count', '')
        # Must be "0" (real count), NOT "3,847" (hardcoded fake)
        self.assertEqual(doc_count, '0',
                         f"Expected '0' for empty DB, got '{doc_count}'")

    def test_counter_matches_real_count(self):
        """When docs exist, counter must match the actual DB count."""
        for i in range(5):
            PolicyDocument.objects.create(
                doc_type='privacy',
                company_name=f'Company {i}',
                content='Test content',
            )
        response = self.client.get(reverse('policies:home'))
        self.assertEqual(response.status_code, 200)
        doc_count = response.context.get('doc_count', '')
        self.assertEqual(doc_count, '5',
                         f"Expected '5', got '{doc_count}'")

    def test_counter_with_thousands_separator(self):
        """Counter must be human-readable with comma separators for large numbers."""
        # Create enough docs to trigger thousands separator
        for i in range(1500):
            PolicyDocument.objects.create(
                doc_type='privacy',
                company_name=f'Company {i}',
                content='Test',
            )
        response = self.client.get(reverse('policies:home'))
        doc_count = response.context.get('doc_count', '')
        self.assertIn(',', doc_count,
                      f"Expected comma-separated number, got '{doc_count}'")
        self.assertEqual(doc_count, '1,500')

    def test_no_hardcoded_fallback_in_code(self):
        """The string '3,847' must not appear in the home view code."""
        import inspect
        from policies import views
        source = inspect.getsource(views.home)
        self.assertNotIn('3,847', source,
                         "Hardcoded '3,847' fallback must be removed")


class TestHomepageTemplateRendersCounter(TestCase):
    """The counter must appear in the rendered HTML."""

    def test_homepage_shows_counter(self):
        """Homepage HTML must include the doc count — real number, not fake."""
        PolicyDocument.objects.create(
            doc_type='terms',
            company_name='TestCo',
            content='Terms content',
        )
        client = Client()
        response = client.get(reverse('policies:home'))
        content = response.content.decode()
        # Must contain the real count
        self.assertIn('1', content)
        # Must NOT contain the fake number
        self.assertNotIn('3,847', content,
                         "Hardcoded '3,847' must not appear in homepage HTML")
