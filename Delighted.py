import gspread
from oauth2client.service_account import ServiceAccountCredentials
import math
import time


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sleeptime = 10
writecount = 0


# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
file = client.open("NPS template - Spring Break 2020")

worksheet_list = file.worksheets()
sheetnumbers = len(worksheet_list)

for tab in range(1, sheetnumbers):
    if tab > 1:
        time.sleep(sleeptime)
        
    sheet = file.get_worksheet(tab)

    # Extract and print all of the values
##    list_of_hashes = sheet.get_all_records()
##    print(list_of_hashes)

    for column in range(3, 11):
        if(sheet.cell(2, column).value):

            trendID = sheet.cell(2, column).value
            
            import delighted
            delighted.api_key = DELIGHTED_API_KEY
            tags = ['Accommodation', 'Bag delays', 'Check-in', 'Communications', 'Experience', 'Flight Comms', 'Flights', 'Food', 'Missold', 'Operations', 'Price', 'Safety', 'Shuttles', 'Staff', 'Tech']
            n = 1

            c_accom = 0
            cpos_accom = 0
            cneg_accom = 0

            c_bags = 0
            cpos_bags = 0
            cneg_bags = 0

            c_check = 0
            cpos_check = 0
            cneg_check = 0

            c_comms = 0
            cpos_comms = 0
            cneg_comms = 0

            c_exper = 0
            cpos_exper = 0
            cneg_exper = 0

            c_fcomms = 0
            cpos_fcomms = 0
            cneg_fcomms = 0

            c_flight = 0
            cpos_flight = 0
            cneg_flight = 0

            c_food = 0
            cpos_food = 0
            cneg_food = 0

            c_missold = 0
            cpos_missold = 0
            cneg_missold = 0

            c_operations = 0
            cpos_operations = 0
            cneg_operations = 0

            c_price = 0
            cpos_price = 0
            cneg_price = 0

            c_safety = 0
            cpos_safety = 0
            cneg_safety = 0

            c_shuttle = 0
            cpos_shuttle = 0
            cneg_shuttle = 0

            c_staff = 0
            cpos_staff = 0
            cneg_staff = 0

            c_tech = 0
            cpos_tech = 0
            cneg_tech = 0

            pos_mentions = []
            neg_mentions = []


            while len(delighted.SurveyResponse.all(per_page = 100, page = n, trend = trendID)) > 0:
                responses = delighted.SurveyResponse.all(per_page = 100, page = n, trend = trendID)
                print(len(responses))
                
                for i in range(len(responses)):
                    if(str(responses[i]['tags']).find(str(tags[0])))>-1:
                        c_accom += 1
                        if(responses[i]['score'])>8:
                          cpos_accom += 1
                        elif(responses[i]['score'])<7:
                          cneg_accom += 1

                    if(str(responses[i]['tags']).find(str(tags[1])))>-1:
                        c_bags += 1
                        if(responses[i]['score'])>8:
                          cpos_bags += 1
                        elif(responses[i]['score'])<7:
                          cneg_bags += 1
                

                    if(str(responses[i]['tags']).find(str(tags[2])))>-1:
                        c_check += 1
                        if(responses[i]['score'])>8:
                          cpos_check += 1
                        elif(responses[i]['score'])<7:
                          cneg_check += 1
                 

                    if(str(responses[i]['tags']).find(str(tags[3])))>-1:
                        c_comms += 1
                        if(responses[i]['score'])>8:
                          cpos_comms += 1
                        elif(responses[i]['score'])<7:
                          cneg_comms += 1
                  

                    if(str(responses[i]['tags']).find(str(tags[4])))>-1:
                        c_exper += 1
                        if(responses[i]['score'])>8:
                          cpos_exper += 1
                        elif(responses[i]['score'])<7:
                          cneg_exper += 1
                  

                    if(str(responses[i]['tags']).find(str(tags[5])))>-1:
                        c_fcomms += 1
                        if(responses[i]['score'])>8:
                          cpos_fcomms += 1
                        elif(responses[i]['score'])<7:
                          cneg_fcomms += 1
                 

                    if(str(responses[i]['tags']).find(str(tags[6])))>-1:
                        c_flight += 1
                        if(responses[i]['score'])>8:
                          cpos_flight += 1
                        elif(responses[i]['score'])<7:
                          cneg_flight += 1
                    

                    if(str(responses[i]['tags']).find(str(tags[7])))>-1:
                        c_food += 1
                        if(responses[i]['score'])>8:
                          cpos_food += 1
                        elif(responses[i]['score'])<7:
                          cneg_food += 1
                    

                    if(str(responses[i]['tags']).find(str(tags[8])))>-1:
                        c_missold += 1
                        if(responses[i]['score'])>8:
                          cpos_missold += 1
                        elif(responses[i]['score'])<7:
                          cneg_missold += 1
                       

                    if(str(responses[i]['tags']).find(str(tags[9])))>-1:
                        c_operations += 1
                        if(responses[i]['score'])>8:
                          cpos_operations += 1
                        elif(responses[i]['score'])<7:
                          cneg_operations += 1
                      

                    if(str(responses[i]['tags']).find(str(tags[10])))>-1:
                        c_price += 1
                        if(responses[i]['score'])>8:
                          cpos_price += 1
                        elif(responses[i]['score'])<7:
                          cneg_price += 1
                    

                    if(str(responses[i]['tags']).find(str(tags[11])))>-1:
                        c_safety += 1
                        if(responses[i]['score'])>8:
                          cpos_safety += 1
                        elif(responses[i]['score'])<7:
                          cneg_safety += 1
                    

                    if(str(responses[i]['tags']).find(str(tags[12])))>-1:
                         c_shuttle += 1
                         if(responses[i]['score'])>8:
                          cpos_shuttle += 1
                         elif(responses[i]['score'])<7:
                          cneg_shuttle += 1
                        

                    if(str(responses[i]['tags']).find(str(tags[13])))>-1:
                         c_staff += 1
                         if(responses[i]['score'])>8:
                          cpos_staff += 1
                         elif(responses[i]['score'])<7:
                          cneg_staff += 1
                          
                       
                    if(str(responses[i]['tags']).find(str(tags[14])))>-1:
                         c_tech += 1
                         if(responses[i]['score'])>8:
                          cpos_tech += 1
                         elif(responses[i]['score'])<7:
                          cneg_tech += 1    

                n += 1

            pos_mentions.append(cpos_accom)
            neg_mentions.append(cneg_accom)

            pos_mentions.append(cpos_bags)
            neg_mentions.append(cneg_bags)

            pos_mentions.append(cpos_check)
            neg_mentions.append(cneg_check)

            pos_mentions.append(cpos_comms)
            neg_mentions.append(cneg_comms)

            pos_mentions.append(cpos_exper)
            neg_mentions.append(cneg_exper)

            pos_mentions.append(cpos_fcomms)
            neg_mentions.append(cneg_fcomms)

            pos_mentions.append(cpos_flight)
            neg_mentions.append(cneg_flight)

            pos_mentions.append(cpos_food)
            neg_mentions.append(cneg_food)

            pos_mentions.append(cpos_missold)
            neg_mentions.append(cneg_missold)

            pos_mentions.append(cpos_operations)
            neg_mentions.append(cneg_operations)

            pos_mentions.append(cpos_price)
            neg_mentions.append(cneg_price)

            pos_mentions.append(cpos_safety)
            neg_mentions.append(cneg_safety)

            pos_mentions.append(cpos_shuttle)
            neg_mentions.append(cneg_shuttle)

            pos_mentions.append(cpos_staff)
            neg_mentions.append(cneg_staff)

            pos_mentions.append(cpos_tech)
            neg_mentions.append(cneg_tech)



            nps_values = []

            
            if c_accom > 0:
                nps_accom = 100*((cpos_accom - cneg_accom)/c_accom)
                nps_values.append(nps_accom)

            if c_bags > 0:
                nps_bags = 100*((cpos_bags - cneg_bags)/c_bags)
                nps_values.append(nps_bags)
                
            if c_check > 0:
                nps_check = 100*((cpos_check - cneg_check)/c_check)
                nps_values.append(nps_check)
                
            if c_comms > 0:
                nps_comms = 100*((cpos_comms - cneg_comms)/c_comms)
                nps_values.append(nps_comms)
                
            if c_exper > 0:
                nps_exper = 100*((cpos_exper - cneg_exper)/c_exper)
                nps_values.append(nps_exper)
                
            if c_fcomms > 0:
                nps_fcomms = 100*((cpos_fcomms - cneg_fcomms)/c_fcomms)
                nps_values.append(nps_fcomms)
                
            if c_flight > 0:
                nps_flight = 100*((cpos_flight - cneg_flight)/c_flight)
                nps_values.append(nps_flight)
                
            if c_food > 0:
                nps_food = 100*((cpos_food - cneg_food)/c_food)
                nps_values.append(nps_food)
                
            if c_missold > 0:
                nps_missold = 100*((cpos_missold - cneg_missold)/c_missold)
                nps_values.append(nps_missold)
                
            if c_operations > 0:
                nps_operations = 100*((cpos_operations - cneg_operations)/c_operations)
                nps_values.append(nps_operations)
                
            if c_price > 0:
                nps_price = 100*((cpos_price - cneg_price)/c_price)
                nps_values.append(nps_price)
                
            if c_safety > 0:
                nps_safety = 100*((cpos_safety - cneg_safety)/c_safety)
                nps_values.append(nps_safety)
                
            if c_shuttle > 0:
                nps_shuttle = 100*((cpos_shuttle - cneg_shuttle)/c_shuttle)
                nps_values.append(nps_shuttle)
                
            if c_staff > 0:
                nps_staff = 100*((cpos_staff - cneg_staff)/c_staff)
                nps_values.append(nps_staff)

            if c_tech > 0:
                nps_tech = 100*((cpos_tech - cneg_tech)/c_tech)
                nps_values.append(nps_tech)



            for jj in range(len(pos_mentions)):
                sheet.update_cell(11 + jj, column, pos_mentions[jj])
                writecount += 1

            for kk in range(len(neg_mentions)):
                sheet.update_cell(30 + kk, column, neg_mentions[kk])
                writecount += 1




            prom_perc = delighted.Metrics.retrieve(trend = trendID)['promoter_percent']
            detr_perc = delighted.Metrics.retrieve(trend = trendID)['detractor_percent']
            nps = delighted.Metrics.retrieve(trend = trendID)['nps']
            response_count = delighted.Metrics.retrieve(trend = trendID)['response_count']

            sheet.update_cell(4, column, nps)
            sheet.update_cell(5, column, round(prom_perc, 0))
            sheet.update_cell(6, column, round(detr_perc, 0))
            sheet.update_cell(7, column, response_count)
            writecount += 4

        else:
            continue

print("Write count = ", writecount)
