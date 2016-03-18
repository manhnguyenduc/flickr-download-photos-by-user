
import flickr_api as Flickr
import sys
import os

from dateutil import parser
import argparse
import json

api_key = 'a326a9e78e94a...'
api_secret = 'a3d21aee...'

Flickr.set_keys(api_key = api_key, api_secret = api_secret)


def donwload_user(user_id, page_num=None):
    
    p = Flickr.Person(id=user_id)
    

    photos_c = p.getPublicPhotos()
    
    print 'total images %d' % photos_c.info.total
    print 'total pages %d' % photos_c.info.pages
    
    if page_num > photos_c.info.pages or page_num is None:
        page_num = photos_c.info.pages
   

    print 'num page for download %s' % page_num
    dirname = user_id.replace('@', "_")
    if not os.path.exists(dirname):
        os.mkdir(dirname)
        print 'make dirname %s' % dirname

    page = 1 
    while page <= page_num:
        photos = p.getPublicPhotos(page=page)

        for photo in photos:
            print photo.getPhotoFile()
            fname = dirname + '/' + photo.title + '.jpg'
            # print fname
            photo.save(fname)
        page += 1
    
def find_by_url(url):
    u = Flickr.Person
    user_id = u.findByUrl(url)
    return user_id.id

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description='Downloads Flickr photo user.\n'
        '\n'
        'To use it you need to get your own Flickr API key here:\n'
        'https://www.flickr.com/services/api/misc.api_keys.html\n'
        '\n'
        '  download a given set:\n'
        '  > {app} -u https://www.flickr.com/photos/ericwong888 \n'
        '\n'
        .format(app=sys.argv[0])
    )
    parser.add_argument('-u', '--url', type=str, metavar='URL',
                        help='Download the given user')

    parser.add_argument('-p', '--page', type=int, metavar='PAGE',
                        help='Number page for download')
    


    args = parser.parse_args()

    if args.url:
        user_id = find_by_url(args.url)
        donwload_user(user_id, args.page)

    parser.print_help()

    return 1


if __name__ == '__main__':
    sys.exit(main())

