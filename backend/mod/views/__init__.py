from .view_article import ArticleList, ArticleDetail
from .view_blog import BlogList, BlogDetail
from .view_notification import NotificationListView, NotificationUpdateView
from .post_view import PostList, PostDetail
from .login_view import LoginView
from .signup_view import UserSignupView
from .searchview import SearchUserView
from .profileview import EditProfileView

__all__ = [
    'ArticleList', 'ArticleDetail',
    'BlogList', 'BlogDetail',
    'PostList', 'PostDetail',
    'NotificationListView', 'NotificationUpdateView',
    'LoginView',
    'UserSignupView',
    'SearchUserView',
    'EditProfileView',
]