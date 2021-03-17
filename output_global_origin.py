#!
# coding=utf-8
import ViconNexus

vicon = ViconNexus.ViconNexus()

def globalaxis():
    vicon.CreateModeledMarker(SubjectName,"GlobalO")
    GO, exists = vicon.GetModelOutput(SubjectName,"GlobalO")
    for i in range(framecount):
        exists[i] = True
        GO[0][i] = 0
        GO[1][i] = 0
        GO[2][i] = 0
    else:
        exists[i] = False
    vicon.SetModelOutput(SubjectName,"GlobalO",GO,exists)

print("Create Global Origin")

# extract the subject name, this is needed to get the model ouputs and to create the modelled markers 
SubjectName = vicon.GetSubjectNames()[0] 
# extract the frame count to determine the length of the created the modelled markers  
framecount = vicon.GetFrameCount()
# extract modeloutput names, this is needed to ensure the outputs are not in the list already
mpnames = vicon.GetModelOutputNames(SubjectName)

if "GlobalO" in mpnames:
    print ("Check modelled marker list under subject names for GlobalO")

else:
    vicon.CreateModeledMarker(SubjectName,"GlobalO")
    GO, exists = vicon.GetModelOutput(SubjectName,"GlobalO")
    for i in range(framecount):
        exists[i] = True
        GO[0][i] = 0
        GO[1][i] = 0
        GO[2][i] = 0
    else:
        exists[i] = False
    vicon.SetModelOutput(SubjectName,"GlobalO",GO,exists)
    
if "GlobalX" in mpnames:
    print ("Check modelled marker list under subject names for GlobalX")
else:
    vicon.CreateModeledMarker(SubjectName,"GlobalX")
    GX, exists = vicon.GetModelOutput(SubjectName,"GlobalX")
    for i in range(framecount):
        exists[i] = True
        GX[0][i] = 200
        GX[1][i] = 0
        GX[2][i] = 0
    else:
        exists[i] = False
    vicon.SetModelOutput(SubjectName,"GlobalX",GX,exists)

if "GlobalY" in mpnames:
    print ("Check modelled marker list under subject names for GlobalY")
else:
    vicon.CreateModeledMarker(SubjectName,"GlobalY")
    GY, exists = vicon.GetModelOutput(SubjectName,"GlobalY")
    for i in range(framecount):
        exists[i] = True
        GY[0][i] = 0
        GY[1][i] = 200
        GY[2][i] = 0
    else:
        exists[i] = False
    vicon.SetModelOutput(SubjectName,"GlobalY",GY,exists)

if "GlobalZ" in mpnames:
    print ("Check modelled marker list under subject names for GlobalZ")
else:          
    vicon.CreateModeledMarker(SubjectName,"GlobalZ")
    GZ, exists = vicon.GetModelOutput(SubjectName,"GlobalZ")
    for i in range(framecount):
        exists[i] = True
        GZ[0][i] = 0
        GZ[1][i] = 0
        GZ[2][i] = 200
    else:
        exists[i] = False
    vicon.SetModelOutput(SubjectName,"GlobalZ",GZ,exists)