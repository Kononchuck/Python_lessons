from google_images_search import GoogleImagesSearch
import os

# you can provide API key and CX using arguments,
# or you can set environment variables: GCS_DEVELOPER_KEY, GCS_CX
#key = os.environ.get('AIzaSyC09J-iyjKouLdTJ87LneJf7SVIkdkht80')
#cx  = os.environ.get('15150e9d8f5197eb6')
#gis = GoogleImagesSearch(key, cx)
gis = GoogleImagesSearch('AIzaSyC09J-iyjKouLdTJ87LneJf7SVIkdkht80', '15150e9d8f5197eb6')
# define search params
# option for commonly used search param are shown below for easy reference.
# For param marked with '##':
#   - Multiselect is currently not feasible. Choose ONE option only
#   - This param can also be omitted from _search_params if you do not wish to define any value
_search_params = {
    'q'       : 'Persian cat',
    'num'     : 1,
    'fileType': 'jpg',
}
gis.search(search_params=_search_params, path_to_dir='/media/den/D/Pycharm')

# for image in gis.results():
#     image.dowload('/media/den/D/Pycharm')
#     image.resize(500, 500)  # resize downloaded image

for image in gis.results():
    print(image.url)