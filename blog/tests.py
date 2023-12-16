from django.test import TestCase, LiveServerTestCase
from django.conf import settings
from .models import BlogPost
from datetime import datetime, timezone
from parameterized import parameterized
from django.utils import timezone
from django.db.utils import IntegrityError, DataError
import pytz
from unittest.mock import patch, Mock

"""
    BlogPost tests
"""
class TestBlogPosts(TestCase):
    TEST_HEADLINE_VALUE = "An Example Blog Post Headline"
    TEST_AUTHOR_VALUE = "David Scheuermann"
    TEST_PUBLISHED_DATETIME_VALUE = timezone.make_aware(datetime(2023, 1, 23, 0, 0, 0), pytz.timezone(settings.TIME_ZONE))
    TEST_MODIFIED_DATETIME_VALUE = timezone.make_aware(datetime(2023, 1, 23, 0, 0, 0), pytz.timezone(settings.TIME_ZONE))
    TEST_FEATURED_IMAGE_VALUE = "/path/to/image"
    TEST_SUMMARY_VALUE = "This is a summary"
    TEST_BODY_VALUE = "<p>This is the article body</p>"

    # test BlogPost
    @parameterized.expand(
        [
            # No headline
            (
                None,
                TEST_AUTHOR_VALUE,
                TEST_FEATURED_IMAGE_VALUE,
                TEST_PUBLISHED_DATETIME_VALUE,
                TEST_MODIFIED_DATETIME_VALUE,
                TEST_SUMMARY_VALUE,
                TEST_BODY_VALUE
            ),
            # No author
            (
                TEST_HEADLINE_VALUE,
                None,
                TEST_FEATURED_IMAGE_VALUE,
                TEST_PUBLISHED_DATETIME_VALUE,
                TEST_MODIFIED_DATETIME_VALUE,
                TEST_SUMMARY_VALUE,
                TEST_BODY_VALUE
            ),
            # No published_datetime
            (
                TEST_HEADLINE_VALUE,
                TEST_AUTHOR_VALUE,
                TEST_FEATURED_IMAGE_VALUE,
                None,
                TEST_MODIFIED_DATETIME_VALUE,
                TEST_SUMMARY_VALUE,
                TEST_BODY_VALUE
            ),
            # No modified datetime
            (
                TEST_HEADLINE_VALUE,
                TEST_AUTHOR_VALUE,
                TEST_FEATURED_IMAGE_VALUE,
                TEST_PUBLISHED_DATETIME_VALUE,
                None,
                TEST_SUMMARY_VALUE,
                TEST_BODY_VALUE
            ),
            # No headline, author, published_datetime, or modified_datetime
            (
                None,
                None,
                TEST_FEATURED_IMAGE_VALUE,
                None,
                None,
                TEST_SUMMARY_VALUE,
                TEST_BODY_VALUE
            ),
            # No headline, author, or published_datetime
            (
                None,
                None,
                TEST_FEATURED_IMAGE_VALUE,
                None,
                TEST_MODIFIED_DATETIME_VALUE,
                TEST_SUMMARY_VALUE,
                TEST_BODY_VALUE
            ),
            # No headline, author
            (
                None,
                None,
                TEST_FEATURED_IMAGE_VALUE,
                TEST_PUBLISHED_DATETIME_VALUE,
                TEST_MODIFIED_DATETIME_VALUE,
                TEST_SUMMARY_VALUE,
                TEST_BODY_VALUE
            ),
            # No headline, published_datetime
            (
                None,
                TEST_AUTHOR_VALUE,
                TEST_FEATURED_IMAGE_VALUE,
                None,
                TEST_MODIFIED_DATETIME_VALUE,
                TEST_SUMMARY_VALUE,
                TEST_BODY_VALUE
            ),
            # No headline, modified_datetime
            (
                None,
                TEST_AUTHOR_VALUE,
                TEST_FEATURED_IMAGE_VALUE,
                TEST_PUBLISHED_DATETIME_VALUE,
                None,
                TEST_SUMMARY_VALUE,
                TEST_BODY_VALUE
            ),
            # No headline, author, modified_datetime
            (
                None,
                None,
                TEST_FEATURED_IMAGE_VALUE,
                TEST_PUBLISHED_DATETIME_VALUE,
                None,
                TEST_SUMMARY_VALUE,
                TEST_BODY_VALUE
            ),
            # No author, published_datetime
            (
                TEST_HEADLINE_VALUE,
                None,
                TEST_FEATURED_IMAGE_VALUE,
                None,
                TEST_MODIFIED_DATETIME_VALUE,
                TEST_SUMMARY_VALUE,
                TEST_BODY_VALUE
            ),
            # No author, published_datetime, modified_datetime
            (
                TEST_HEADLINE_VALUE,
                None,
                TEST_FEATURED_IMAGE_VALUE,
                None,
                None,
                TEST_SUMMARY_VALUE,
                TEST_BODY_VALUE
            ),
            # No author, modified_datetime
            (
                TEST_HEADLINE_VALUE,
                None,
                TEST_FEATURED_IMAGE_VALUE,
                TEST_PUBLISHED_DATETIME_VALUE,
                None,
                TEST_SUMMARY_VALUE,
                TEST_BODY_VALUE
            ),
        ]
    )
    def test_when_BlogPost_required_values_are_None_then_raise_IntegrityError(self, headline: str, author: str, featured_image: str, published_datetime: timezone, modified_datetime: timezone, summary: str, body: str):
        # Arrange
        # Should have a headline, author, published_datetime
        # summary, body
        blog_post = BlogPost(
            headline=headline,
            author=author,
            featured_image=featured_image,
            published_datetime=published_datetime,
            modified_datetime=modified_datetime,
            summary=summary,
            body=body
        )


        # Act and Assert
        self.assertRaises(IntegrityError, blog_post.save)

    # required values are blank, then raise ValidationError
    @parameterized.expand(
        [
            # Headline blank
            (
                "",
                TEST_AUTHOR_VALUE,
                TEST_FEATURED_IMAGE_VALUE,
                TEST_PUBLISHED_DATETIME_VALUE,
                TEST_MODIFIED_DATETIME_VALUE,
                TEST_SUMMARY_VALUE,
                TEST_BODY_VALUE
            ),
            # author blank
            (
                TEST_HEADLINE_VALUE,
                "",
                TEST_FEATURED_IMAGE_VALUE,
                TEST_PUBLISHED_DATETIME_VALUE,
                TEST_MODIFIED_DATETIME_VALUE,
                TEST_SUMMARY_VALUE,
                TEST_BODY_VALUE
            ),
            # headline, author blank
            (
                "",
                "",
                TEST_FEATURED_IMAGE_VALUE,
                TEST_PUBLISHED_DATETIME_VALUE,
                TEST_MODIFIED_DATETIME_VALUE,
                TEST_SUMMARY_VALUE,
                TEST_BODY_VALUE
            ),
        ]
    )
    def test_when_required_values_are_empty_then_raise_IntegrityError(self, headline: str, author: str, featured_image: str, published_datetime: timezone, modified_datetime: timezone, summary: str, body: str):
        # Arrange
        blog_post = BlogPost(
            headline=headline,
            author=author,
            featured_image=featured_image,
            published_datetime=published_datetime,
            modified_datetime=modified_datetime,
            summary=summary,
            body=body
        )

        # Act and Assert
        self.assertRaises(IntegrityError, blog_post.save)

    # optional values are None or empty, then save blog_post without error
    #
    @parameterized.expand(
        [
            # No featured image
            (
                TEST_HEADLINE_VALUE,
                TEST_AUTHOR_VALUE,
                None,
                TEST_PUBLISHED_DATETIME_VALUE,
                TEST_MODIFIED_DATETIME_VALUE,
                TEST_SUMMARY_VALUE,
                TEST_BODY_VALUE
            ),
            # No summary
            (
                TEST_HEADLINE_VALUE,
                TEST_AUTHOR_VALUE,
                TEST_FEATURED_IMAGE_VALUE,
                TEST_PUBLISHED_DATETIME_VALUE,
                TEST_MODIFIED_DATETIME_VALUE,
                None,
                TEST_BODY_VALUE
            ),
            # No body
            (
                TEST_HEADLINE_VALUE,
                TEST_AUTHOR_VALUE,
                TEST_FEATURED_IMAGE_VALUE,
                TEST_PUBLISHED_DATETIME_VALUE,
                TEST_MODIFIED_DATETIME_VALUE,
                TEST_SUMMARY_VALUE,
                None
            ),
            # No featured_image, summary
            (
                TEST_HEADLINE_VALUE,
                TEST_AUTHOR_VALUE,
                None,
                TEST_PUBLISHED_DATETIME_VALUE,
                TEST_MODIFIED_DATETIME_VALUE,
                None,
                TEST_BODY_VALUE
            ),
            # No featured_image, body
            (
                TEST_HEADLINE_VALUE,
                TEST_AUTHOR_VALUE,
                TEST_FEATURED_IMAGE_VALUE,
                TEST_PUBLISHED_DATETIME_VALUE,
                TEST_MODIFIED_DATETIME_VALUE,
                TEST_SUMMARY_VALUE,
                None
            ),
            # No featued_image, summary, body
            (
                TEST_HEADLINE_VALUE,
                TEST_AUTHOR_VALUE,
                None,
                TEST_PUBLISHED_DATETIME_VALUE,
                TEST_MODIFIED_DATETIME_VALUE,
                None,
                None
            ),
        ]
    )
    def test_when_optional_values_are_None_or_empty_then_save_BlogPost(self, headline: str, author: str, featured_image: str, published_datetime: timezone, modified_datetime: timezone, summary: str, body: str):
        # Arrange
        blog_post = BlogPost(
            headline=headline,
            author=author,
            featured_image=featured_image,
            published_datetime=published_datetime,
            modified_datetime=modified_datetime,
            summary=summary,
            body=body
        )

        # Act
        blog_post.save()

        # Assert
        # django.db.models._state.adding is True if object not saved to db
        # False otherwise
        self.assertFalse(blog_post._state.adding)

    # blog post datetime default is current datetime
    # utils.now wraps around timezone.now for easy testing default values
    @patch('blog.utils.timezone.now')
    def test_when_BlogPost_saved_without_published_datetime_then_save_with_published_datetime_as_now(self, mock_timezone_now: Mock):
        # Arrange
        NOW_DATETIME = datetime(2023, 1, 1, 0, 0, 0, 0, tzinfo=timezone.utc)
        mock_timezone_now.return_value = NOW_DATETIME
        blog_post = BlogPost(
            headline=TestBlogPosts.TEST_HEADLINE_VALUE,
            author=TestBlogPosts.TEST_AUTHOR_VALUE,
            featured_image=TestBlogPosts.TEST_FEATURED_IMAGE_VALUE,
            # Cannot pass published_datetime value even if None
            # published_datetime=None,
            summary=TestBlogPosts.TEST_SUMMARY_VALUE,
            body=TestBlogPosts.TEST_BODY_VALUE
        )

        # Act
        blog_post.save()

        # Assert
        self.assertEqual(blog_post.published_datetime, NOW_DATETIME)


    # blog post modified time default is also the current datetime
    # utils.now wraps around timezone.now for easy testing default values
    @patch('blog.utils.timezone.now')
    def test_when_BlogPost_saved_without_modified_datetime_then_save_with_modified_datetime_as_now(self, mock_timezone_now: Mock):
        # Arrange
        NOW_DATETIME = datetime(2023, 1, 1, 0, 0, 0, 0, tzinfo=timezone.utc)
        mock_timezone_now.return_value = NOW_DATETIME

        blog_post = BlogPost(
            headline=TestBlogPosts.TEST_HEADLINE_VALUE,
            author=TestBlogPosts.TEST_AUTHOR_VALUE,
            featured_image=TestBlogPosts.TEST_FEATURED_IMAGE_VALUE,
            # Cannot pass modified_datetime value even if None
            # modified_datetime=None,
            summary=TestBlogPosts.TEST_SUMMARY_VALUE,
            body=TestBlogPosts.TEST_BODY_VALUE
        )

        # Act
        blog_post.save()

        # Assert
        self.assertEqual(blog_post.modified_datetime, NOW_DATETIME)

    # headline should not exceed max length of 128 chars
    def test_save_when_headline_exceeds_128_chars_then_raise_IntegrityError(self):
        # Arrange
        headline = "This is a headline that is 257 characters and I will this " \
            + "to test that 256 chars is a good limit. I do not believe a " \
            + "good headline can possibly have more than 256 characters. " \
            + "That is what I definitely believe would be too long. Ok I think " \
            + "256 is probably th"
        blog_post = BlogPost(
            headline=headline,
            author=TestBlogPosts.TEST_AUTHOR_VALUE,
            featured_image=TestBlogPosts.TEST_FEATURED_IMAGE_VALUE,
            # Cannot pass published_datetime value even if None
            # published_datetime=None,
            summary=TestBlogPosts.TEST_SUMMARY_VALUE,
            body=TestBlogPosts.TEST_BODY_VALUE
        )


        # Act and Assert
        self.assertRaises(DataError, blog_post.save)

    # str function should return headline and date
    def test_str_then_return_headline_and_date(self):
        # Arrange
        blog_post = BlogPost(
            headline=TestBlogPosts.TEST_HEADLINE_VALUE,
            author=TestBlogPosts.TEST_AUTHOR_VALUE,
            featured_image=TestBlogPosts.TEST_FEATURED_IMAGE_VALUE,
            # Cannot pass published_datetime value even if None
            # published_datetime=None,
            summary=TestBlogPosts.TEST_SUMMARY_VALUE,
            body=TestBlogPosts.TEST_BODY_VALUE
        )

        # Act
        post_str = str(blog_post)

        # Assert
        self.assertEqual(post_str, f"{blog_post.headline} ({blog_post.modified_datetime.date()})")

    # validate body can contain rich text
    def test_save_when_body_contains_rich_text_then_rich_text_saved_succesfully(self):
        # Arrange
        rich_text_content = """
        This is **bold** text.
        This is _italic_ text.
        - Item 1
        - Item 2
          - Subitem 2.1
        Visit [example.com](http://example.com).
        ![Alt text](http://example.com/image.jpg)
        """
        blog_post: BlogPost = BlogPost(
            headline=TestBlogPosts.TEST_HEADLINE_VALUE,
            author=TestBlogPosts.TEST_AUTHOR_VALUE,
            featured_image=TestBlogPosts.TEST_FEATURED_IMAGE_VALUE,
            # Cannot pass published_datetime value even if None
            # published_datetime=None,
            summary=TestBlogPosts.TEST_SUMMARY_VALUE,
            body=rich_text_content
        )

        # Act
        blog_post.save()

        # Assert
        retrieved_post = BlogPost.objects.get(id=blog_post.id)
        self.assertEqual(retrieved_post.body, rich_text_content)