import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="my webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
     r = requests.get(url)
     if r.status_code !=200:
          return st.title("myre")
     return r.json()


lottie_coding2=load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_ot9fofi5.json")
lottie_coding=load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_qmrxbp0w.json")

#----HEADER SECTION----
with st.container():
    a,b=st.columns(2)
    with a:
         st.subheader("Its me abinemmanuelvinu :wave:")
         st.title("Fitness Freak")
         st.write("Hi, I'm Abin, a student from India who has been consistently working out for a year to achieve my fitness goals. I'm inspired by fitness icons like Tom Platz, Jo Lindner, and David Laid, and I'm here to share some of my workout routines with you.")
         st.write("I've learned a lot about fitness over the past year, and I'm excited to share my knowledge with you. I'll be covering everything from my favorite exercises to my meal plan. I hope you find my tips helpful, and I'm always happy to answer any questions you have.")
         st.write("So, whether you're a beginner or a seasoned pro, I invite you to join me on my fitness journey. Together, we can achieve our goals and become the best versions of ourselves.")
    with b:
         st_lottie(lottie_coding, height=400, key="coding")

with st.container():
     st.write("---")
     st.title("MY WORKOUT ROUTINE")
     st.subheader("Warm up:")
     st.write("-Push Ups 10x3sets")       
     st.write("-Pull Ups (Manual/Mechine)10-20x3sets")       
     Monday,Tuesday,Wednesday=st.columns(3)
     with Monday:
          st.title("Monday")
          st.subheader("Chest and Triceps")           
          st.write(
               """
               **Chest**-:                                 
                    Flat(Bench press/Dumbbell press) 15x3sets:
                    Incline(Bench press/Dumbbell press) 15x3sets:
                    Decline(Bench press/Dumbbell press) 15x3sets:
                    Fly(Dumbbell/Cable/Peck deck) 15x3sets:     
                    High Cable Flyes 15x3sets:                
                    Low Cable Flyes 15x3sets:                
                    Seated Machine Press 20x3sets:                  
                **Triceps**-:                                  
                    Weighted Dips/Machine Dips 15x3sets:                           
                    Tricep Pushdowns(Rope/Straight Bar/V Bar) 15x3sets:          
                """
                )
     with Tuesday:
          st.title("Tuesday")
          st.subheader("Back and Biceps")    
          st.write(
               """
               **Back**-:                                           
                    Deadlift/Bent Rows 10-15x3sets:                                                  
                    Tbar Rows 15x3sets:                            
                    Lat Pulldown 15x3sets:                       
                    Seated Cable Rows 15x3sets:                                         
                    Seated Mechine Row/Dumbbell Row 15x3sets:
                    Seated Single Lat Pulldown 15x3sets:                                 
                    Standing Lat Pulldown 15x3sets:                                  
               **Biceps**-:                                                     
                    Wide,Medium,Close Gripped EZ Bar Curls (7+7+7)x3sets:                         
                    Single Dumbbell Curls 15x3sets:                                          
                    """
                    )
     with Wednesday:
          st.title("Wednesday")
          st.subheader("Shoulder and Triceps")
          st.write(
               """
               **Shoulder**-:                                             
                    Military Press 15x3sets:                                                     
                    Shoulder Dumbbell Press 15x3sets:                                                            
                    Arnold Dumbbell Press 15x3:                                                  
                    Shoulder Press On Calf Raise Mechine 15x3sets:                                       
                    Lateral Flyes(Mechine/Dumbbell/Cable) 30-40x3sets:                                      
                    Front Raise(Weight plates/Cable) 10-20x3sets:                                           
                    Bend Over Flyes/Face Pulls 15x3sets:                                               
               **Triceps**-:                                                   
                    Weighted Dips/Machine Dips 15x3sets:                           
                    Tricep Pushdowns(Rope/Straight Bar/V Bar) 15x3sets:                   
               """
               )
     
     Thursday,Friday,Saturday=st.columns(3)
     with Thursday:
          st.title("Thursday")
          st.subheader("Arms Day")
          st.write(
               """
               **Triceps**-:
               Weighted/Mechine Dips 15x3sets:                                                      
               Close Grip Press/Skull Crusher 15x3sets:                                             
               Tricep Pushdowns (rope/Straight Bar/V Bar) 15x3sets:                                            
               Dumbbell Kickbacks 15x3sets:                                                    
               **Biceps**-:                                                                    
               Dumbbell Curls Single 15x3sets:                                                             
               Wide,Medium,Close Gripped EZ Bar Curls (7+7+7)x3sets:                         
               Cable Curls/Preacher Curls(Mechine/Manual) 15x3sets:                                                          
               Seated Cable Curls 15x3sets:                                                                                      
               """
               )
     with Friday:
          st.title("Friday")
          st.subheader("Chest Day")
          st.write(
               """
               **Chest**-:                                              
               Flat Bench Press 15x3sets:                                             
               Flat Dumbbell Press 15x3sets:                                               
               Flat Dumbbell Fly 15x3sets:                                                  
               Incline Mechine Press 15x3sets:                                                 
               Cable/Mechine Flys 15x3sets:                                            
               Seated Chest Press 20x3sets:                                               
               """
               )
     with Saturday:
          st.title("Saturday")
          st.subheader("Leg Day")
          st.write(
               """
               **Leg**-:                                                                  
               Manual Squats 15x4sets:                                                               
               Sumo Squats 15x3sets:                                                                    
               Leg Extensions 20x3sets:                                                           
               Leg Curls 15x3sets:                                                              
               Seated Calf Raises 15x3sets:                                                              
               
               For Pumb-:                                                                                
               Cable Curls/Weigthed Dips 15x2sets:                                                              
               """
               )     
with st.container():
     st.write("---")
     j,e=st.columns(2)
     with j:
          st.subheader("Warm Down")
          st.write("I used to warm down my body with a forearm workout.")
          st.subheader("Preworkouts")
          st.write("I used to fuel my workouts with a nutrient-rich shake made with milk, oats, peanut butter, and banana.")
          st.subheader("conclusion")
          st.write(""" "**NEVER SKIP LEG DAYS**" """)   
          st.write("I couldn't have achieved my fitness goals without the help of my incredible gym partner, **Vasudev Sreekanth**.")
          st.markdown("[Follow me](https://www.instagram.com/abinemmanuelvinu/)")
     with e:
          st_lottie(lottie_coding2, height=400, key="coding2")