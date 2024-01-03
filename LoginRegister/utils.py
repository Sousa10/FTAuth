from .models import LinkClickCount

def increment_click_count(app_name):
    link_click_count, created = LinkClickCount.objects.get_or_create(link_name=app_name)
    link_click_count.click_count += 1
    link_click_count.save()
    return link_click_count.click_count
