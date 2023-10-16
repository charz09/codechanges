import os
import json
import spacy
import geopy.distance
from spacy.kb import KnowledgeBase
from geopy.geocoders import Nominatim
# single comment 1
class Caption: #caption class

    caption = None
    toponyms = None
    toponym_true_positives = 0
    toponym_false_positives = 0
    toponym_false_negatives = 1
    location_true_positives = 0
    location_false_positives = 0
    location_false_negatives = 1
    def __init__(
            self,
            json_object): #class constructor
        self.caption = json_object["caption"] 
        self.ground_truth_toponym = json_object["ground truth toponym"]
        self.toponyms = []

        nlp = spacy.load("en_core_web_sm")
        doc = nlp(self.caption)

        for ent in doc.ents:
            if ent.label_ in ["FAC", "GPE", "LOC"]:
                self.toponyms.append(Toponym(cap=self, string=ent.text))

        for loc in self.toponyms: 
            if loc.toponym == self.ground_truth_toponym:
                loc.toponym_true_positives = True
                self.toponym_true_positives = 1
                self.toponym_false_negatives = 0
            else:
                loc.toponym_true_positives = False
                self.toponym_false_positives += 1
class Toponym: #toponym class
    toponym = None
    toponym_true_positives = None
    location_true_positives = None
    def __init__(self, cap, string): #class constructor
        self.toponym = string
# single comment 2
def get_captions(file_name): #retrieves captions from the json file 
    caps = []
    with open(file_name, "r") as file:
        data = json.load(file)
    for loc in data:
        caps.append(Caption(loc))
    return caps
def final(): #provides output
    captions = get_captions("json-capLatLong.json")
    caption_details = ""
    true_positives = 0
    false_positives = 0
    false_negatives = 0

    for cap in captions:
        caption_details += "Caption: " + cap.caption + "\t""\t"

        if len(cap.toponyms) == 0:
            caption_details += "No entities detected."
        else:
            caption_details += "Entities: "
            for toponym in cap.toponyms:
                caption_details += toponym.toponym + ","

        true_positives += cap.toponym_true_positives
        false_positives += cap.toponym_false_positives
        false_negatives += cap.toponym_false_negatives

        caption_details += "\n"

    precision = true_positives / (true_positives + false_positives)
    recall = true_positives / len(captions)
    f1 = 2 * precision * recall / (precision + recall)
# single comment 3
    print(caption_details)
    print("Number of true positives: " + str(true_positives))
    print("Number of false positives: " + str(false_positives))
    print("Number of false negatives: " + str(false_negatives))
    print("Precision: " + str(precision))
    print("Recall: " + str(recall))
    print("F1: " + str(f1))



final()
