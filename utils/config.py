import json

from sys import implementation

class Config:
    palette = None
    color_objective = None
    selections = None
    max_population_size = None
    max_generations = None
    cross_over = None
    mutation = None
    implementation = None
    runs = None
    
    @staticmethod
    def load_from_json(json_file):
        if Config.palette is not None:
            return
        with open(json_file) as json_file:
            data = json.load(json_file)
        Config.palette = data['palette']
        Config.color_objective = data['color_objective']
        Config.selections = data['selections']
        Config.max_population_size = data['max_population_size']
        Config.max_generations = data['max_generations']
        Config.cross_over = data['cross_over']
        Config.mutation = data['mutation']
        Config.implementation = data['implementation']
        Config.runs = data['runs']
    
    @staticmethod
    def get_palette_color_amount():
        return len(Config.palette)
