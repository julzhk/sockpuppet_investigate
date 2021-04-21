from sockpuppet.reflex import Reflex


class IndustryReflex(Reflex):
    def increment(self, step=1):
        print('increment')
        self.count = int(self.session.get('count', 1)) + step
        self.request.session['count'] = self.count

    def reset(self, step=1):
        self.count = 0
        self.session['count'] = 0
        self.request.session['selected_companies'] = ''

    def selected(self):
        print('selected')
        print(self.element.dataset.get("industry", ''))
        self.industry = self.element.dataset.get('industry', 1)
        self.request.session['industry'] = self.industry

    def company(self):
        print('company selected')
        this_company = self.element.dataset["company"]
        print(this_company)
        self.request.session['selected_companies'] += f'{this_company}, '
