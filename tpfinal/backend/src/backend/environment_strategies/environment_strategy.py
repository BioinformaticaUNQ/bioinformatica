from Bio.Align.Applications import ClustalwCommandline
class LinuxClustalRunner():

    def run(self, file_path):
        clustalw_cline = ClustalwCommandline(infile=file_path)
        # assert os.path.isfile(clustalw), "Clustal W executable missing"
        stdout, stderr = clustalw_cline()


class WindowsClustalRunner():

    def run(self, file_path):
        clustalw_path = 'C:\Program Files (x86)\ClustalW2\clustalw2.exe'
        clustalw_cline = ClustalwCommandline(clustalw_path, infile=file_path)
        # assert os.path.isfile(clustalw), "Clustal W executable missing"
        stdout, stderr = clustalw_cline()