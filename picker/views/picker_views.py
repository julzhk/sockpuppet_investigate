from django.views.generic.base import TemplateView


def is_fresh_page(context):
    return not context.get('stimulus_reflex')


DATA = {'credit': ['acme', 'boom', 'catcard'],
        'banks': ['Starling', 'Big Bank', 'Co-op Bank', 'Debt bank'],
        'supermarkets': ['tescos', 'sainsbury', 'asda'],
        'other': ['o2', '03', 'o4'], }


class PickerIndustryView(TemplateView):
    template_name = 'industry.html'

    def get_context_data(self, *args, **kwargs):
        print('get context in view')
        context = super().get_context_data(*args, **kwargs)
        if is_fresh_page(context):
            print('fresh')
        context['count'] = self.request.session.get('count', 3)
        context['industry'] = self.request.session.get('industry', 'None')
        context['industry_list'] = DATA.keys()
        context['companies'] = DATA.get(context['industry'], [])
        context['selected_companies'] = self.request.session.get('selected_companies', '')
        context['TEMPLATE'] = 'base.html'

        return context


class AuthorizeView(TemplateView):
    template_name = 'authorize.html'

    def get_context_data(self, *args, **kwargs):
        print('get context in view')
        context = super().get_context_data(*args, **kwargs)
        context['TEMPLATE'] = 'base.html'

        return context
