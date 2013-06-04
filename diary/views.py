#-*- coding:utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.template import RequestContext
from diary.models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


def Index(request):
	if request.user.is_authenticated():
		uid = request.user.id
	else:
		uid=1
	ctx = {'uid':uid}
	return render_to_response('diary/index.html', ctx,
		context_instance=RequestContext(request))

def Privacy(request):
	uid = request.user.id
	ctx = {'uid':uid}
	return render_to_response('diary/privacy.html', ctx,
		context_instance=RequestContext(request))

def Service(request):
	uid = request.user.id
	ctx = {'uid':uid}
	return render_to_response('diary/service.html', ctx,
		context_instance=RequestContext(request))

def About(request):
	uid = request.user.id
	ctx = {'uid':uid}
	return render_to_response('diary/about.html', ctx,
		context_instance=RequestContext(request))

@csrf_exempt
@login_required
def Feedback(request):
	uid = request.user.id
	success = False
	if request.method == "POST":
		user = request.user
		title = request.POST.get('f_title', '')
		content = request.POST.get('f_content', '')
		if title and content:
			new_feed = Feed(user=user, title=title, content=content)
			new_feed.save()
			success = True
	ctx = {'success':success, 'uid':uid}
	return render_to_response('diary/feedback.html', ctx,
		context_instance=RequestContext(request))



def MonthDisplay(request, uid):
	"""validate user"""
	if request.user.is_anonymous():
		return HttpResponse("Please Login First!")
	if request.user.id != long(uid):
		return HttpResponse("You can not read other's Diary!")
	"""validate user"""

	"""Cover Function"""
	jan = '/static/default/Jan.jpg'
	feb = '/static/default/Feb.jpg'
	mar = '/static/default/Mar.jpg'
	apr = '/static/default/Apr.jpg'
	may = '/static/default/May.jpg'
	jun = '/static/default/Jun.jpg'
	jul = '/static/default/Jul.jpg'
	aug = '/static/default/Aug.jpg'
	sep = '/static/default/Sep.jpg'
	oct = '/static/default/Oct.jpg'
	nov = '/static/default/Nov.jpg'
	dec = '/static/default/Dec.jpg'
	default_covers = [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]
	user_covers = Cover.objects.filter(user__id=uid, year=2013).order_by('month')
	covers = default_covers
	for user_cover in user_covers:
		index = int(user_cover.month) - 1
		covers[index] = user_cover.imgurl

	ctx = {'uid':uid, 'covers':covers}
	return render_to_response('diary/month_display.html', ctx,
		context_instance=RequestContext(request))



@csrf_exempt
def MyDiary(request, uid, month):
	"""validate user"""
	if request.user.is_anonymous():
		return HttpResponse("Please Login First!")
	if request.user.id != long(uid):
		return HttpResponse("You can not read other's Diary!")
	"""validate user"""
 
	diaries = Diary.objects.filter(user__id=uid)
	select_month_diary = diaries.filter(date__month=month).order_by('date')

	"""Ajax start"""
	if request.is_ajax():
		flag = request.POST.get('flag')

		"""New"""
		if flag == 'new':
			new_date = request.POST.get('date')
			new_content = request.POST.get('content').strip()
			if (new_date and new_content):
				try:
					new_diary = Diary(user_id=uid, date=new_date, content=new_content)
					new_diary.save()
					ret = 1
				except:
					ret = 2
			else:
				ret = 0
			return HttpResponse(ret)

		"""Delete"""
		if flag == 'delete':
			delete_date = request.POST.get('date')
			delete_content = request.POST.get('content')
			try:
				select_diary = select_month_diary.filter(date=delete_date, content=delete_content)[0]
				select_diary.delete()
				ret = 1
			except:
				ret = 0
			return	HttpResponse(ret)

		"""Edit"""
		if flag == 'edit':
			old_date = request.POST.get('old_date')
			old_content = request.POST.get('old_content')
			new_date = request.POST.get('new_date')
			new_content = request.POST.get('new_content')
			select_diary = select_month_diary.filter(date=old_date, content=old_content)[0]
			try:
				select_diary.date = new_date
				select_diary.content = new_content
				select_diary.save()
				ret = 1
			except:
				ret = 0
			return HttpResponse(ret)

		"""Cover"""
		if flag == 'cover':
			year = 2013
			imgurl = request.POST.get('imgurl')
			try:
				cover = Cover(user_id=uid, year=year, month=month, imgurl=imgurl)
				cover.save()
				ret = 1
			except:
				ret = 0
			return HttpResponse(ret)

	"""Ajax end"""
	
	ctx = {'select_month_diary':select_month_diary, 'uid':uid, 'month':month}
	return render_to_response('diary/mydiary.html', 
		ctx, context_instance=RequestContext(request))


