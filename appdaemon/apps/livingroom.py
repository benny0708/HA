import appdaemon.plugins.hass.hassapi as hass
import datetime, time


#
# Hellow World App
#
# Args:
#

class LivingroomWorld(hass.Hass):

    def initialize(self):
        self.log("Starting livingroom Service")
#        self.listen_state(self.bedlight_off,"binary_sensor.dev31_button1s", new = "on")
#        self.listen_state(self.bedlight_off,"binary_sensor.dev32_button1s", new = "on")
#        self.set_state("sensor.dev26_5_hold",state="0")
#        self.listen_state(self.ventilation_toggle,"sensor.dev26_5_hold", new = "1")
        self.listen_state(self.light_vitrine_toggle,"sensor.taster_licht_hennes")

#    def bedlight_off(self, entity, attribute, old, new,kwargs):
#        self.log("Switch bedlight lights off")
#        self.turn_off("light.joiner_bedroom")

    def light_vitrine_toggle(self, entity, attribute, old, new,kwargs):
        self.log("Toggle ambi light vitrine")
        self.toggle("light.ambi_licht_vitrine")

#    def ventilation_toggle(self, entity, attribute, old, new,kwargs):
#        self.set_state("sensor.dev26_5_hold",state="0")
#        self.toggle("switch.dev26_gpio_15") # ventilator
