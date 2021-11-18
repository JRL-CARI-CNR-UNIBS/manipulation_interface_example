#!/usr/bin/env python3

import pymongo
import pprint
import rospy

from std_msgs.msg import String
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db_param = rospy.get_param("/mongo_db_name")
print(db_param)
db = client[db_param]

go_to_collection     = db.go_to_locations
boxes_collection     = db.boxes
slots_collection     = db.slots
groups_collection    = db.groups
objects_collection   = db.objects
tasks_collection     = db.tasks_properties
recipes_collection   = db.recipes

if __name__ == '__main__':
	rospy.init_node('prova', anonymous=True)

	go_to_collection.delete_many({})
	go_to_param = rospy.get_param("/go_to_location")
	go_to_collection.insert_many(go_to_param)

	boxes_collection.delete_many({})
	boxes_param = rospy.get_param("/inbound/boxes")
	boxes_collection.insert_many(boxes_param)

	slots_collection.delete_many({})
	slots_param = rospy.get_param("/outbound/slots")
	slots_collection.insert_many(slots_param)

	groups_collection.delete_many({})
	groups_param = rospy.get_param("/outbound/slots_group")
	groups_collection.insert_many(groups_param)

	objects_collection.delete_many({})
	objects_param = rospy.get_param("/manipulation_object_types")
	objects_collection.insert_many(objects_param)

	tasks_collection.delete_many({})
	tasks_param = rospy.get_param("/multi_skills/tasks")
	tasks_collection.insert_many(tasks_param)

	recipes_collection.delete_many({})
	recipes_param = rospy.get_param("/multi_skills/recipes")
	recipes_collection.insert_many(recipes_param)
