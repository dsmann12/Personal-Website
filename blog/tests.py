from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import BlogPost
from datetime import datetime
from parameterized import parameterized
from django.utils import timezone
from ..personal_website import settings
import pytz

"""
    BlogPost tests
"""
class TestBlogPosts(TestCase):
    TEST_HEADLINE_VALUE = "An Example Blod Post Headline"
    TEST_AUTHOR_VALUE = "David Scheuermann"
    TEST_PUBLISHED_DATETIME_VALUE = timezone.make_aware(datetime(2023, 1, 23, 0, 0, 0), pytz.timezone(settings.TIME_ZONE))
    TEST_FEATURED_IMAGE_VALUE = "/path/to/image"
    TEST_SUMMARY_VALUE = "This is a summary"
    TEST_BODY_VALUE = "<p>This is the article body</p>"

    # test BlogPost
    # TODO: I should test multiple configurations of required values missing
    @parameterized(
        # No headline
        [
            None,
            TEST_AUTHOR_VALUE,
            TEST_FEATURED_IMAGE_VALUE,
            TEST_PUBLISHED_DATETIME_VALUE,
            TEST_SUMMARY_VALUE,
            TEST_BODY_VALUE
        ],
        # No author
        [
            TEST_HEADLINE_VALUE,
            None,
            TEST_FEATURED_IMAGE_VALUE,
            TEST_PUBLISHED_DATETIME_VALUE,
            TEST_SUMMARY_VALUE,
            TEST_BODY_VALUE
        ],
        # No featured image,
        [
            TEST_HEADLINE_VALUE,
            TEST_AUTHOR_VALUE,
            None,
            TEST_PUBLISHED_DATETIME_VALUE,
            TEST_SUMMARY_VALUE,
            TEST_BODY_VALUE
        ],
        # No published_datetime
        [
            TEST_HEADLINE_VALUE,
            TEST_AUTHOR_VALUE,
            TEST_FEATURED_IMAGE_VALUE,
            None,
            TEST_SUMMARY_VALUE,
            TEST_BODY_VALUE
        ],
        # No headline, author, featured_image, or published_datetime
        [
            None,
            None,
            None,
            None,
            TEST_SUMMARY_VALUE,
            TEST_BODY_VALUE
        ],
        # No headline author, featured_image
        [
            None,
            TEST_AUTHOR_VALUE,
            None,
            TEST_PUBLISHED_DATETIME_VALUE,
            TEST_SUMMARY_VALUE,
            TEST_BODY_VALUE
        ],
        # No headline, author
        [
            None,
            None,
            TEST_FEATURED_IMAGE_VALUE,
            TEST_PUBLISHED_DATETIME_VALUE,
            TEST_SUMMARY_VALUE,
            TEST_BODY_VALUE
        ],
        # No healine, featured_image
        [
            None,
            TEST_AUTHOR_VALUE,
            None,
            TEST_PUBLISHED_DATETIME_VALUE,
            TEST_SUMMARY_VALUE,
            TEST_BODY_VALUE
        ],
        # No headline, published_datetime
        [
            None,
            TEST_AUTHOR_VALUE,
            TEST_FEATURED_IMAGE_VALUE,
            None,
            TEST_SUMMARY_VALUE,
            TEST_BODY_VALUE
        ],
        # No author, featured_image
        [
            TEST_HEADLINE_VALUE,
            None,
            None,
            TEST_PUBLISHED_DATETIME_VALUE,
            TEST_SUMMARY_VALUE,
            TEST_BODY_VALUE
        ],
    )
    def test_when_BlogPost_missing_required_values_then_raise_ValidationError(self, headline: str, author: str, featured_image: str, published_datetime: timezone, summary: str, body: str):
        # Arrange
        # Should have a headline, author, published_datetime, featured_image
        # summary, body
        blog_post = BlogPost(
            headline=headline,
            author=author,
            featured_image=featured_image,
            published_datetime=published_datetime,
            summary=summary,
            body=body
        )

        # Act and Assert
        self.assertRaises(ValidationError, blog_post.save())

    # blog post datetime default is current datetime
    # validate types?
    # saves to database and gets an ID
    # if item already exists in database, then overwrite
    # str function should return headline 