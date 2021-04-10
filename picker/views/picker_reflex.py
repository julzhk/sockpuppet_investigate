from django.views.generic.base import TemplateView


class PickerReflexView(TemplateView):
    template_name = 'picker_reflex.html'

    def get_context_data(self, *args, **kwargs):
        print('get context in view')
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.request.session.get('count', 3)
        context['loop'] = range(0, 200 * context['count'])
        context['inc_template'] = 'included.html'

        if context.get('count', 0) > 4:
            context['inc_template'] = 'included2.html'
            context['msg'] = 'overload'
        return context
