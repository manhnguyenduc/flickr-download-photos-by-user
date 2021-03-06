import flickr_api as Flickr
import sys
import os
import errno

import argparse

import flickr_key

api_key = flickr_key.api_key
api_secret = flickr_key.api_secret

Flickr.set_keys(api_key=api_key, api_secret=api_secret)


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def donwload_user(user_id, page_num=None, dirname=None):
    p = Flickr.Person(id=user_id)

    photos_c = p.getPublicPhotos()

    print 'total images %d' % photos_c.info.total
    print 'total pages %d' % photos_c.info.pages

    if page_num > photos_c.info.pages or page_num is None:
        page_num = photos_c.info.pages

    print 'num page for download %s' % page_num
    if dirname is None:
        dirname = user_id.replace('@', "_")
    else:
        dirname = dirname + '/' + user_id.replace('@', "_")

    if not os.path.exists(dirname):
        mkdir_p(dirname)
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
                    '  download user photo:\n'
                    '  > {app} -u https://www.flickr.com/photos/ericwong888 \n'
                    '\n'
            .format(app=sys.argv[0])
    )
    parser.add_argument('-u', '--url', type=str, metavar='URL',
                        help='Download the given user')

    parser.add_argument('-p', '--page', type=int, metavar='PAGE',
                        help='Number page for download')

    parser.add_argument('-d', '--dirname', type=str, metavar='DIRNAME',
                        help='Directory for save')

    args = parser.parse_args()

    if args.url:
        user_id = find_by_url(args.url)
        donwload_user(user_id, args.page, args.dirname)

    parser.print_help()

    return 1


if __name__ == '__main__':
    sys.exit(main())
