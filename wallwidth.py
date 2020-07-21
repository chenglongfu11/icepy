import basic
from util11 import *
import time
import math


class WallWidth:

    # direct to zone 1
    def zone_geo_obj(self, building):
        zone1 = None
        keyword = 'Zone'
        childdict = basic.showChildrenDict(building)

        for k, v in childdict.items():
            if v.count(keyword) >0:
                zone1 = ida_get_named_child(building, v)
                break

        if zone1 is None:
            print('The zone is not detected, please select it manually:')
            print(childdict)
            inp = input('Insert the name of zone:')
            zone1 = ida_get_named_child(building, str(inp))

        z1_geo = ida_get_named_child(zone1, 'GEOMETRY')

        return z1_geo

    def get_corners(self, geo):
        corner = None
        geo_childdict = basic.showChildrenDict(geo)
        for k, v in geo_childdict.items():
            if v.count('CORNERS') >0:
                corner = ida_get_named_child(geo, 'CORNERS')
                break

        if corner is None:
            print('The corner is not detected, please select it manually:')
            print(geo_childdict)
            inp = input('Insert the name of zone:')
            corner = ida_get_named_child(geo, str(inp))

        time.sleep(1)
        element_val = ida_get_value(corner)

        wall_coor = []
        try:
            for item in element_val:
                item_ls = []
                item_ls.append(item['value'][0]['value'])  # x
                item_ls.append(item['value'][1]['value'])  # y
                wall_coor.append(item_ls)
        except:
            print('The corner method went wrong')

        return wall_coor

    def parse_wallwidth(self, wall_coor):

        wall_width_ls = []

        for i in range(len(wall_coor)):
            x0 = wall_coor[i][0]
            y0 = wall_coor[i][1]
            if i == len(wall_coor) - 1:
                x1 = wall_coor[0][0]
                y1 = wall_coor[0][1]
            else:
                x1 = wall_coor[i + 1][0]
                y1 = wall_coor[i + 1][1]

            wall_width = math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)
            wall_width_ls.append(round(wall_width, 3))  # 3 digits

        print(wall_width_ls)
        return wall_width_ls





