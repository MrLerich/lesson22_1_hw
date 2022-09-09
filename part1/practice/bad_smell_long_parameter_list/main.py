class Unit:
    def _get_speed(self):
        if self.movement == "fly":
            return self.speed * 1.2
        elif self.movement == "crawl":
            return self.speed * 0.5

    def move(self, direction):
        speed = self._get_speed()

        if direction == 'UP':
            self.field.set_unit(y=self.y + speed, x=self.x, unit=self)

        elif direction == 'DOWN':
            self.field.set_unit(y=self.y - speed, x=self.x, unit=self)

        elif direction == 'LEFT':
            self.field.set_unit(y=self.y, x=self.x - speed, unit=self)

        elif direction == 'RIGTH':
            self.field.set_unit(y=self.y, x=self.x + speed, unit=self)
