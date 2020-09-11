from icepy.basic import *
import icepy.zoneclone as zoneclone
import icepy.wwr as wwr
import icepy.runscript as runscript
import icepy.simulation as simulation
import icepy.readhtml as readhtml
from os import path
import time

class IDM(object):
  idm = '.idm'
  building = None
  pid = None


  def __init__(self, folder, fname):
    self.folder = folder   # 'D:\\ide_mine\\changing\\'
    if fname.count('.idm') >0:
        path_ls = fname.split('\\')
        self.fname = path_ls[-1].strip('.idm')  # 'ut1_1'
    else:
        self.fname = fname  # 'ut1_1'

    self.apath = self.folder + self.fname + self.idm  # 'D:\\ide_mine\\changing\\ut1_1.idm'
    if len(self.apath) > 0:
        if not path.exists(self.apath):
            print('The idm file doesn\'t exist ! Please initiate the object again! ')

    self.zoneClone = zoneclone.ZoneClone()
    self.wwrPro = wwr.WWR()
    self.runscript = runscript.RunScript()
    self.simulate = simulation.Simulation()
    self.read_html = readhtml.Readhtml()


  def openfile(self, fname= None):
      if fname == None:
          fname = self.fname
      file_path = self.folder + fname + self.idm
      self.building, self.pid = connectIDA(file_path)
      return self.building

  def openfile_path(self, file_path):
      self.building, self.pid = connectIDA(file_path)
      return self.building

  def saveas(self, path = ''):
      if self.check_bld():
          res = saveIDM(self.building, path)
          return res
      else:
          pass

  def close(self):
      if self.pid == None:
          pass
      else:
        killprocess(self.pid)

  def save_close(self, path = ''):
        if self.saveas(path):
          self.close()

  def check_bld(self):
    if self.building == None:
        print('No building object detected.')
        return False
    return True


  def zoneclone(self, floor_ht, num_floors):

      result, new_name = self.zoneClone.clone_zone(self.building, floor_ht, num_floors)

      new_path = self.folder + new_name + '.idm'
      return result,new_path


    # Save to the target path, folder
  def zoneclone_save(self, floor_ht, num_floors, folder = None):
      result, new_path = self.zoneclone(floor_ht, num_floors)
      if folder == None:
          folder = self.folder

      self.saveas(new_path)
      return new_path



  def applyscript(self, num_floors, wins=[], doors=[]):
      script = self.runscript.generate_script(wins, doors, num_floors)
      self.runscript.apply_script(self.building, script)


    # Options: 0: proportional distribution   1: fixed height 1.5m  2: multiple standard windows
  def applywwr_new(self, wwr, wall_width_list, floor_ht, name, option = 0):
        """
      Apply new WWR ratio and create windows for the building.
      :param wwr:
      :param wall_width_list: list of wall width
      :param floor_ht: floor height ( ceiling height)
      :param name: idm file name
      :param option:  0: proportional distribution   1: fixed height 1.5m  2: multiple standard windows
      :return: new file path
      """
        new_path = ''
        if self.check_bld():
            if option == 0:
                new_path, bld = self.wwrPro.wwr2_proportional(self.building, wwr, wall_width_list, floor_ht, self.folder, name)
            elif option == 1:
                new_path, bld = self.wwrPro.wwr2_fixed_ht(self.building, wwr, wall_width_list, floor_ht, self.folder, name)
            elif option == 2:
                new_path, bld = self.wwrPro.wwr2_multi(self.building, wwr, wall_width_list, floor_ht, self.folder, name)
            else:
                print('Wrong input for option.')

        time.sleep(2)
        return new_path


  def applywwr_change(self, wwr, wall_width_list, floor_ht, name):
      if self.check_bld():
          self.wwrPro.wwr2(self.building, wwr, wall_width_list, floor_ht, self.folder, name)
      time.sleep(2)


  def simulation_bld(self, new_path = None):
      # Do simulation for current building
      if new_path == None:
          new_path = self.apath

      if self.check_bld():
          self.simulate.simulation_bld(self.building, new_path)


  def simulation_path(self, path):
        """
      Do simulation for idm models
      :param path of idm models
      :return: comutational results and paths of generated html reports
      """

        computational, html_dict = self.simulate.simulation_path_w_html(path)
        return computational, html_dict


    # Relative path for files in the same folder
    def simulation_rela(self, fname):
        file_path = self.folder + fname
        computational, html_dict = self.simulation_path(file_path)
        return computational, html_dict


  def sequential_simulation_wwr(self, paths, wwrs):
      """
        Run simulations for idm models with particular wwr values
      :param wwrs: list of wwrs
      :param name: name of the new file
      :return:
      """

      computational, html_dicts = self.simulate.sequantial_w_html(paths, wwrs)

      return computational, html_dicts



  def html_report_bld(self, folder, filename):
      """
        Generate html report particularly with user defined folder and name
      :param folder:
      :param filename:
      :return:
      """
      res = self.read_html.genehtml_bld(self.building, folder, filename)
      return res


  def html_report_path(self, filepath):
      res = self.read_html.genehtml_path(filepath)
      return res

  # 不用 plot结果的方法进来了
  # Only worable for this building object

    # Read CSV file and return list of dicts
    def read_csv(self, file_path):
        items = self.runscript.read_csv(file_path)
        return items

    def read_csv_rela(self, relative_file_path):
        file_path = self.folder + relative_file_path
        items = self.read_csv(file_path)
        return items

















