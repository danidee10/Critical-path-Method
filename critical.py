import sys
from itertools import zip_longest as zip
class criticalPath:

    def __init__(self):
        '''
        Initialize all the variables we're going to use to calculate the critical path
        '''
        self.id = None
        self.predecessor = tuple()
        self.duration = None
        self.est = None
        self.lst = None
        self.resource = None
        self.all_objects = list()
        self.level = [[], []]

    def __lt__(self, other):
        return other.id > self.id

    def __gt__(self, other):
        return self.id > other.id


    def get_properties(self):

        '''
        This method gets all the input from the user and stores the
        activity name as a string, the predecessor as a tuple and the duration
        as an integer
        '''
        while True:
            object_list = list()
            try:
                num_act = input('How many activities are in the project:\n')
                num_act  = int(num_act)
                break
            except ValueError:
                print('{} is not an integer please enter a valid number\n'.format(num_act))
                continue
            except KeyboardInterrupt:
                print('The user quit the application')
                sys.exit()
        for i in range(num_act):
            name = input('what is the name of the activity {}:\n'.format(i+1))
            activity = criticalPath()
            predecessor = input('what is the predecessor(s) of the activity:\n')
            predecessor = tuple(predecessor.replace(',', ''))
            while True:
                try:
                    duration = input('what is the duration of the activity:\n')
                    duration = int(duration)

                    est = input('Enter the activity\'s earliest starting time:\n')
                    est = int(est)

                    lst = input('Enter the activity\'s latest starting time:\n')
                    lst = int(lst)

                    resource = input('What are the resources available:\n')
                    resource = int(resource)
                    break
                except ValueError:
                    print('{} is not an integer please enter a valid number\n'.format(duration))
                    continue
                except KeyboardInterrupt:
                    print('The user quit the application')
                    sys.exit()



            '''sets the properties of the objects from what was gotten from the user'''
            activity.set_properties(name, predecessor, duration, est, lst, resource)

            object_list.append(activity)

            self.all_objects.append(activity)



        return object_list

    def set_properties(self, name, predecessor, duration, est, lst, resource):
        self.id = name
        self.predecessor = predecessor
        self.duration = duration
        self.est = est
        self.lst = lst
        self.resource = resource


    def get_starting_nodes(self):
        '''
        gets the starting nodes/activities and puts them individually into a nested list
        '''

        list_node = list()
        ls = self.get_properties()
        for i in ls:
            for a in i.predecessor:
                if '0' in a:
                    myls = list()
                    myls.append(i)
                    list_node.append(myls)

        return list_node

    def get_branches(self, starting_nodes, all_objects):
        '''
        Do a forward pass and checks all the activities individually and connects
        them to their matching predecessors
        '''

        for ind, st_nodes in enumerate(starting_nodes):
            for node in all_objects:
                if st_nodes[-1].id in node.predecessor:
                    starting_nodes[ind].append(node)

                    '''
                    If the length of a starting node is more than one check the second to the last activity
                    if it has other successors, if so then connect it to the matching predecessor
                    '''

                elif len(st_nodes) > 1:
                    if st_nodes[-2].id in node.predecessor:
                        new_path = list()
                        new_path.append(node)
                        starting_nodes.append(new_path)

        return starting_nodes


    def patch_branches(self, starting_nodes, all_objects):
        '''
        do a backward pass and patch all the nodes/activities which have not been connected to their predecessor
        from the previous calculation
        '''
        for ind, final_result in enumerate(starting_nodes):
                while final_result[0].predecessor != ('0',):
                    for node in all_objects:
                        if node.id in final_result[0].predecessor:
                            starting_nodes[ind].insert(0, node)


        '''
        for some reason duplicates are generated when calculating all the possible paths,
        this block of code removes all duplicates in the nested list
        '''
        all_paths = list()
        for path in starting_nodes:
            if sorted(path) not in all_paths:
                all_paths.append(sorted(path))

        return all_paths


'''class for resource levelling'''
class level(criticalPath):
    def __init__(self):
        pass

    def level_est(self, all_objects):
        for activity in all_objects:
            resource = activity.resource
            est = activity.est
            duration = activity.duration

            if est == 0:
                for count in range(duration):
                    activity.level[0].append(resource)
            else:
                while True:
                    if len(activity.level[0]) < est:
                        activity.level[0].append(0)
                    else:
                        break
                for count in range(duration):
                    activity.level[0].append(resource)


    def level_lst(self, all_objects):
        for activity in all_objects:
            resource = activity.resource
            lst = activity.lst
            duration = activity.duration

            if lst == 0:
                for count in range(duration):
                    activity.level[1].append(resource)
            else:
                while True:
                    if len(activity.level[1]) < lst-1:
                        activity.level[1].append(0)
                    else:
                        break
                for count in range(duration):
                    activity.level[1].append(resource)

        return all_objects




def main():
    activity = criticalPath()
    starting_nodes = activity.get_starting_nodes()
    all_objects = activity.all_objects

    '''get all the possible branches in the diagram'''
    starting_nodes = activity.get_branches(starting_nodes, all_objects)
    all_paths = activity.patch_branches(starting_nodes, all_objects)


    '''if all_path is not empty then print all the possible paths in the project'''

    if None != all_paths:
        print('The possible paths in the project are')
        for i in all_paths:
            print( '==>'.join(str(a.id) for a in i))

        critical_path = ('==>'.join([path.id for path in max(all_paths, key=lambda ls: sum(obj.duration for obj in ls))]))
        project_duration = ((max([sum([node.duration for node in object]) for object in all_paths])))

        print('The critical path is {} and the project duration is {}'.format(critical_path, project_duration))

    else:
        print('There was a problem calculating the critical path')






    '''All the calculation for the resource levelling class'''

    levelit = level()
    levelit.level_est(all_objects)
    all_objects = levelit.level_lst(all_objects)

    for activity in all_objects:
        print(activity.level,'\n')

    '''list comprehension to add all the values in the est and lst of the objects'''
    result = [[sum(j) for j in zip(*i, fillvalue=0)] for i in zip(*[activity.level for activity in all_objects], fillvalue=[0])]
    print(result)

    total = [[sum(j)] for j in [i for i in result]]
    print(total)

    [print('The resource levelled is {0:.1f} percent'.format(b/a * 100)) for a, b in zip(*total)]




if __name__ == '__main__': main()
