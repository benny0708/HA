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
        self.listen_state(self.delay_ventilation_selector_switch,"binary_sensor.lueftung_low")
        self.listen_state(self.delay_ventilation_selector_switch,"binary_sensor.lueftung_medium")
        self.listen_state(self.delay_ventilation_selector_switch,"binary_sensor.lueftung_high")

    def ventilation_selector_switch(self, entity):
        self.log("Waiting time finished")
        VentLow = self.get_state("binary_sensor.lueftung_low")
        VentMed = self.get_state("binary_sensor.lueftung_medium")
        VentHigh = self.get_state("binary_sensor.lueftung_high")
        if(VentLow == "off" and VentMed == "off" and VentHigh == "off"):
            self.log("Ventilation Off")
            self.call_service("fan/set_speed", entity_id="fan.lueftung", speed="off")
        elif(VentLow == "on" and VentMed == "off" and VentHigh == "off"):
            self.log("Ventilation Speed set to Low")
            self.call_service("fan/set_speed", entity_id="fan.lueftung", speed="low")
        elif(VentLow == "off" and VentMed == "on" and VentHigh == "off"):
            self.log("Ventilation Speed set to Medium")
            self.call_service("fan/set_speed", entity_id="fan.lueftung", speed="medium")
        elif(VentLow == "off" and VentMed == "off" and VentHigh == "on"):
            self.log("Ventilation Speed set to High")
            self.call_service("fan/set_speed", entity_id="fan.lueftung", speed="high")
        else:
            self.log("Error operating selector switch: No position detected")

    def delay_ventilation_selector_switch(self, entity, attribute, old, new,kwargs):
        self.log("Ventilation Selector Switch is operated")
        self.run_in(self.ventilation_selector_switch, 1)
