#!/usr/bin/env python3

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

from std_msgs.msg import String


data_ = pd.read_csv('/home/gauss/Documents/experiment_data/task1.csv')

sizes = [60, 62, 64, 66, 68]
font_scale_ = [3.5]

sns.set(rc={'figure.figsize':(21,15)})

for size_ in sizes:
    for font_scale__ in font_scale_:

        sns.set(font_scale = font_scale__)
        sns.set_style("whitegrid", {'axes.grid' : False})

        ax = sns.barplot(x="interface", y="learning_times", data=data_, capsize=0.5)
        ax.set_ylabel('time[s]',size=size_)
        ax.set_xlabel('interface', size=size_)
        name = 'LeT'
        name = name + str(size_) + '_' + str(font_scale__) + '.png'
        plt.savefig(name)
        plt.clf()

        ax = sns.barplot(x="interface", y="programming_times", data=data_, capsize=0.5)
        ax.set_ylabel('time[s]',size=size_)
        ax.set_xlabel('interface', size=size_)
        name = 'PrT'
        name = name + str(size_) + '_' + str(font_scale__) + '.png'
        plt.savefig(name)
        plt.clf()

        ax = sns.barplot(x="interface", y="programming_questions", data=data_, capsize=0.5)
        ax.set_ylabel('quantity[n]',size=size_)
        ax.set_xlabel('interface', size=size_)
        name = 'PrQ'
        name = name + str(size_) + '_' + str(font_scale__) + '.png'
        plt.savefig(name)
        plt.clf()

        ax = sns.barplot(x="interface", y="test_times", data=data_, capsize=0.5)
        ax.set_ylabel('time[s]',size=size_)
        ax.set_xlabel('interface', size=size_)
        name = 'TeT'
        name = name + str(size_) + '_' + str(font_scale__) + '.png'
        plt.savefig(name)
        plt.clf()

        ax = sns.barplot(x="interface", y="test_numbers", data=data_, capsize=0.5)
        ax.set_ylabel('quantity[n]',size=size_)
        ax.set_xlabel('interface', size=size_)
        name = 'TeN'
        name = name + str(size_) + '_' + str(font_scale__) + '.png'
        plt.savefig(name)
        plt.clf()

        ax = sns.barplot(x="interface", y="test_questions", data=data_, capsize=0.5)
        ax.set_ylabel('quantity[n]',size=size_)
        ax.set_xlabel('interface', size=size_)
        name = 'TeQ'
        name = name + str(size_) + '_' + str(font_scale__) + '.png'
        plt.savefig(name)
        plt.clf()

        ax = sns.barplot(x="interface", y="execution_times", data=data_, capsize=0.5)
        ax.set_ylabel('time[s]',size=size_)
        ax.set_xlabel('interface', size=size_)
        name = 'ExT'
        name = name + str(size_) + '_' + str(font_scale__) + '.png'
        plt.savefig(name)
        plt.clf()

        ax = sns.barplot(x="interface", y="simplicity", data=data_, capsize=0.5)
        ax.set_ylabel('vote[n]',size=size_)
        ax.set_xlabel('interface', size=size_)
        name = 'Comp'
        name = name + str(size_) + '_' + str(font_scale__) + '.png'
        plt.savefig(name)
        plt.clf()

        ax = sns.barplot(x="interface", y="intuitiveness", data=data_, capsize=0.5)
        ax.set_ylabel('vote[n]',size=size_)
        ax.set_xlabel('interface', size=size_)
        name = 'Int'
        name = name + str(size_) + '_' + str(font_scale__) + '.png'
        plt.savefig(name)
        plt.clf()

        ax = sns.barplot(x="interface", y="speed", data=data_, capsize=0.5)
        ax.set_ylabel('vote[n]',size=size_)
        ax.set_xlabel('interface', size=size_)
        name = 'Vel'
        name = name + str(size_) + '_' + str(font_scale__) + '.png'
        plt.savefig(name)
        plt.clf()

        data_ = pd.read_csv('/home/gauss/Documents/experiment_data/task2.csv')

        ax = sns.barplot(x="user", y="learning_times", hue="interface", data=data_)
        ax.set_ylabel('time[s]',size=size_)
        ax.set_xlabel('operator[n]', size=size_)
        name = 'second_LeT'
        name = name + str(size_) + '_' + str(font_scale__) + '.png'
        plt.savefig(name)
        plt.clf()

        ax = sns.barplot(x="user", y="programming_times", hue="interface", data=data_, capsize=0.5)
        ax.set_ylabel('time[s]',size=size_)
        ax.set_xlabel('operator[n]', size=size_)
        name = 'second_PrT'
        name = name + str(size_) + '_' + str(font_scale__) + '.png'
        plt.savefig(name)
        plt.clf()

        ax = sns.barplot(x="user", y="programming_questions", hue="interface", data=data_, capsize=0.5)
        ax.set_ylabel('quantity[n]',size=size_)
        ax.set_xlabel('operator[n]', size=size_)
        name = 'second_PrQ'
        name = name + str(size_) + '_' + str(font_scale__) + '.png'
        plt.savefig(name)
        plt.clf()

        ax = sns.barplot(x="user", y="test_times", hue="interface", data=data_, capsize=0.5)
        ax.set_ylabel('time[s]',size=size_)
        ax.set_xlabel('operator[n]', size=size_)
        name = 'second_TeT'
        name = name + str(size_) + '_' + str(font_scale__) + '.png'
        plt.savefig(name)
        plt.clf()

        ax = sns.barplot(x="user", y="test_numbers", hue="interface", data=data_, capsize=0.5)
        ax.set_ylabel('quantity[n]',size=size_)
        ax.set_xlabel('operator[n]', size=size_)
        name = 'second_TeN'
        name = name + str(size_) + '_' + str(font_scale__) + '.png'
        plt.savefig(name)
        plt.clf()

        ax = sns.barplot(x="user", y="test_questions", hue="interface", data=data_, capsize=0.5)
        ax.set_ylabel('quantity[n]',size=size_)
        ax.set_xlabel('operator[n]', size=size_)
        name = 'second_TeQ'
        name = name + str(size_) + '_' + str(font_scale__) + '.png'
        plt.savefig(name)
        plt.clf()

        ax = sns.barplot(x="user", y="execution_times", hue="interface", data=data_, capsize=0.5)
        ax.set_ylabel('time[s]',size=size_)
        ax.set_xlabel('operator[n]', size=size_)
        name = 'second_ExT'
        name = name + str(size_) + '_' + str(font_scale__) + '.png'
        plt.savefig(name)
        plt.clf()

        ax = sns.barplot(x="user", y="simplicity", hue="interface", data=data_, capsize=0.5)
        ax.set_ylabel('vote[n]',size=size_)
        ax.set_xlabel('operator[n]', size=size_)
        name = 'second_Comp'
        name = name + str(size_) + '_' + str(font_scale__) + '.png'
        plt.savefig(name)
        plt.clf()

        ax = sns.barplot(x="user", y="intuitiveness", hue="interface", data=data_, capsize=0.5)
        ax.set_ylabel('vote[n]',size=size_)
        ax.set_xlabel('operator[n]', size=size_)
        name = 'second_Int'
        name = name + str(size_) + '_' + str(font_scale__) + '.png'
        plt.savefig(name)
        plt.clf()

        ax = sns.barplot(x="user", y="speed", hue="interface", data=data_, capsize=0.5)
        ax.set_ylabel('vote[n]',size=size_)
        ax.set_xlabel('operator[n]', size=size_)
        name = 'second_Vel'
        name = name + str(size_) + '_' + str(font_scale__) + '.png'
        plt.savefig(name)
        plt.clf()


        ax = sns.barplot(x="user", y="reprogramming_times", hue="interface", data=data_, capsize=0.5)
        ax.set_ylabel('time[s]',size=size_)
        ax.set_xlabel('operator[n]', size=size_)
        name = 'ReT'
        name = name + str(size_) + '_' + str(font_scale__) + '.png'
        plt.savefig(name)
        plt.clf()


        ax = sns.barplot(x="user", y="reprogramming_questions", hue="interface", data=data_, capsize=0.5)
        ax.set_ylabel('quantity[n]',size=size_)
        ax.set_xlabel('operator[n]', size=size_)
        name = 'ReQ'
        name = name + str(size_) + '_' + str(font_scale__) + '.png'
        plt.savefig(name)
        plt.clf()


        ax = sns.barplot(x="user", y="second_test_times", hue="interface", data=data_, capsize=0.5)
        ax.set_ylabel('time[s]',size=size_)
        ax.set_xlabel('operator[n]', size=size_)
        name = 'ReTeT'
        name = name + str(size_) + '_' + str(font_scale__) + '.png'
        plt.savefig(name)
        plt.clf()


        ax = sns.barplot(x="user", y="second_test_numbers", hue="interface", data=data_, capsize=0.5)
        ax.set_ylabel('quantity[n]',size=size_)
        ax.set_xlabel('operator[n]', size=size_)
        name = 'ReTeN'
        name = name + str(size_) + '_' + str(font_scale__) + '.png'
        plt.savefig(name)
        plt.clf()


        ax = sns.barplot(x="user", y="second_test_questions", hue="interface", data=data_, capsize=0.5)
        ax.set_ylabel('quantity[n]',size=size_)
        ax.set_xlabel('operator[n]', size=size_)
        name = 'ReTeQ'
        name = name + str(size_) + '_' + str(font_scale__) + '.png'
        plt.savefig(name)
        plt.clf()


        ax = sns.barplot(x="user", y="second_execution_times", hue="interface", data=data_, capsize=0.5)
        ax.set_ylabel('time[s]',size=size_)
        ax.set_xlabel('operator[n]', size=size_)
        name = 'ReExT'
        name = name + str(size_) + '_' + str(font_scale__) + '.png'
        plt.savefig(name)
        plt.clf()
