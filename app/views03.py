from surfer import *

#############################################

# PROTOTYPE 03

#############################################


def results(request):
    error = False
    if 'query' in request.GET:
        query = (request.GET['query']).strip()
        #query = query.strip()
        if not query:
            error = True
        else:
            # VIDEOS
            videos_vids, translations = videos(query)
            videos_len = len(videos_vids)

            return render_to_response('prototype03/results.html', locals())
    return render_to_response('prototype03/results.html', {'error': error})


def main(request):
    return render_to_response('prototype03/index.html', locals())
