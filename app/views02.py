from surfer import *

#############################################

# PROTOTYPE 02

#############################################


def results(request):
    error = False
    if 'query' in request.GET:
        query = (request.GET['query']).strip()
        #query = query.strip()
        if not query:
            error = True
        else:
            # IMAGES
            images_imgs, translations = images(query)
            images_len = len(images_imgs)

            return render_to_response('prototype02/results.html', locals())
    return render_to_response('prototype02/results.html', {'error': error})


def main(request):
    return render_to_response('prototype02/index.html', locals())
