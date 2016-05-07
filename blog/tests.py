from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from .models import Post
from .forms import PostForm


class PostModelTest(TestCase):
    """
    Basic model tests.
    """
    def test_str_representation(self):
        post = Post(title='My First Post')
        self.assertEqual(str(post), post.title)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Post._meta.verbose_name_plural), 'Post Entries')

    def test_upload_location_string(self):
        file_upload = open('blog/davinci.jpg', 'rb')
        form_data = {
            'title': "Cowabunga",
            'body': "The Teenage Mutant Ninja Turtles were my favorire cartoon\
                    characters growing up. Moreover, I loved Michelangelo simply \
                    for the fact he always rode a skateboard and ate pizza.",
            'image': SimpleUploadedFile(file_upload.name, file_upload.read())
        }
        response = self.client.post('/blog/create-post/', form_data, follow=True)
        self.assertEqual(response.status_code, 200)


class PageTests(TestCase):
    """
    Test each page gives valid HTTP responses
    """
    def test_home_page(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_admin_page(self):
        response = self.client.get('/admin/login/?next=/admin/')
        self.assertEqual(response.status_code, 200)

    def test_create_post_page(self):
        response = self.client.get('/blog/create-post/')

        self.assertEqual(response.status_code, 200)
        self.assertTrue('post_form' in response.context)

    def test_update_post_page(self):
        post = PostForm({
                'title': 'American Pie',
                'body': 'If you want to make an apple pie from scratch, you \
                        must first create the universe.'
            })
        self.assertTrue(post.is_valid())
        post.save()
        response = self.client.get('/blog/american-pie/update/')
        self.assertEqual(response.status_code, 200)


class PostFormTest(TestCase):
    """
    Test form submissions
    """
    def test_valid_form(self):
        form = PostForm( {
                'title': 'One Love',
                'body': "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe."
            })
        self.assertTrue(form.is_valid())
        post = form.save()
        self.assertTrue(Post.objects.all().count(), 1)
        self.assertEqual(post.title, 'One Love')
        self.assertEqual(post.body, "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.")
        self.assertEqual(post.get_absolute_url(), '/blog/one-love/')

    def test_empty_form(self):
        post = PostForm({})
        self.assertFalse(post.is_valid())

    def test_2_posts_same_title(self):
        form1 = PostForm( {
                'title': 'Deep Space 9',
                'body': "I'm a rock star among geeks, wonks, and nerds."
            })
        #####
        self.assertTrue(form1.is_valid())
        form1.save()

        form2 = PostForm({
                'title': 'Deep Space 9',
                'body': 'I always hated high-school shows and high-school \
                        movies, because they were always about the cool kids.\
                         It was always about dating and sex, and all the \
                        popular kids, and the good-looking kids. And the \
                        nerds were super-nerdy cartoons, with tape on their \
                        glasses. I never saw "my people" portrayed accurately.'
            })

        self.assertFalse(form2.is_valid())


    def test_update_post_no_title_change(self):

        form_data = {
                'title': 'QA',
                'body': "Quality means doing it right the first time when no one is looking."
            }
        # follow response to account for redirect
        response = self.client.post('/blog/create-post/', form_data, follow=True)
        self.assertContains(response, 'QA')
        self.assertTrue(Post.objects.all().count(), 1)

        form_data = {
                'title': 'QA',
                'body': "First solve the problem, then write the code."
            }
        response = self.client.post('/blog/qa/update/', form_data)
        # updated form data will redirect to post url
        self.assertEqual(response.status_code, 302)
