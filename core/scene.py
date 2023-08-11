import arcade


class Scene():

    def __init__(self):
        self.bg_color = arcade.color.JET
        pass

    def update(self, dt):
        print("Updating Scene")
        pass

    def render(self):
        print("Rendering Scene")
        pass

        
class SceneA(Scene):
    def __init__(self):
        super.__init__()
        self.bg_color = arcade.color.BLUE
        pass

class SceneB(Scene):
    def __init__(self):
        super.__init__()
        self.bg_color = arcade.color.GREEN
        pass

