import appdaemon.plugins.hass.hassapi as hass
import datetime, time


#
# Hellow World App
#
# Args:
#

class VentilationWorld(hass.Hass):

    def initialize(self):
        self.log("Starting Ventilation Service")
        self.listen_state(self.ventilation_selector_switch,"binary_sensor.lueftung_low")
        self.listen_state(self.ventilation_selector_switch,"binary_sensor.lueftung_medium")
        self.listen_state(self.ventilation_selector_switch,"binary_sensor.lueftung_high")

    def ventilation_selector_switch(self, entity, attribute, old, new,kwargs):
        self.log("Ventilation Selector Switch is operated")
        if(self.get_state("binary_sensor.lueftung_low") == "Off" and self.get_state("binary_sensor.lueftung_medium") == "Off" and self.get_state("binary_sensor.lueftung_high") == "Off"):
            self.log("Ventilation Off")
            self.call_service("fan/set_speed", entity_id="fan.lueftung", speed="off")
        elif(self.get_state("binary_sensor.lueftung_low") == "On" and self.get_state("binary_sensor.lueftung_medium") == "Off" and self.get_state("binary_sensor.lueftung_high") == "Off"):
            self.log("Ventilation Speed set to Low")
            self.call_service("fan/set_speed", entity_id="fan.lueftung", speed="low")
        elif(self.get_state("binary_sensor.lueftung_low") == "Off" and self.get_state("binary_sensor.lueftung_medium") == "On" and self.get_state("binary_sensor.lueftung_high") == "Off"):
            self.log("Ventilation Speed set to Medium")
            self.call_service("fan/set_speed", entity_id="fan.lueftung", speed="medium")
        elif(self.get_state("binary_sensor.lueftung_low") == "Off" and self.get_state("binary_sensor.lueftung_medium") == "Off" and self.get_state("binary_sensor.lueftung_high") == "On"):
            self.log("Ventilation Speed set to High")
            self.call_service("fan/set_speed", entity_id="fan.lueftung", speed="high")
        else:
            self.log("Error operating selector switch: No position detected")
