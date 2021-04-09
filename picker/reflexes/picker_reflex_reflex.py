from sockpuppet.reflex import Reflex


class PickerReflexReflex(Reflex):
    def increment(self, step=1):
        print('increment')
        self.count = int(self.session.get('count', 1)) + step
        self.request.session['count'] = self.count

    def reset(self, step=1):
        self.count = 0
        self.session['count'] = 0
