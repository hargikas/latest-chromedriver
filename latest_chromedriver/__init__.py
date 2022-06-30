import pkg_resources

from latest_chromedriver.download_driver import download_only_if_needed
from latest_chromedriver.enviroment import safely_set_chromedriver_path

__version__ = pkg_resources.get_distribution("latest_chromedriver").version
__all__ = ['chrome_info', 'download_driver', 'enviroment']
