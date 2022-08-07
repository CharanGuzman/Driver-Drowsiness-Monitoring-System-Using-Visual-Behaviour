from scipy.spatial import distance as dist
def NLR(drivernose,NOSE_AVERAGE):
    #NOSE_AVERAGE =1.2
    point = dist.euclidean(drivernose[3], drivernose[0])
    nose_np = point / NOSE_AVERAGE
    return nose_np/75