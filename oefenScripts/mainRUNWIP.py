"""

CODE FOLLOWS PEP 8 STYLE

End product should contain:
    - RUN
        - GUI interface where user selects (from dropdown menus):

            - Model architecture to be used
                - options are: CNN own design, CNN mobile net transfer learning, CNN paper (unfinished), CNN Squeezenet (unfinished)

            - Batches to be created (1 or more)
                - nice to have : batches of differing size for now size == 80
                - AQL class of the batch (1,2,3,4 or randomize)
                - after creating displays thumbnail images

            - Access to database with apple stats (select date, time = displays stats of batch)
                - per batch : batch size, batch aql, amount sick blotch scab and normal
                
            - Sjetbot interface to request specific stats (as proof of concept, stats will be easily accesible via drop down menus)
                - retrains on selection (GUI element = button that leads to sjetbot interface)

        - CSV or other database (pandasdf?) containing stats for created batches (by datetime of creation) appended on batch creation
            - batch size, batch aql, amount sick blotch scab and normal
        
        - Sjetbot training OBV resultaten van batch
            - Sjetbot traint (verder) NALV batch generatie    

    
    - BUILD
        - Data Augmentation
        
        - Model training
            - MobilnetV2, CNN own design(paper based), CNN own design pytorch, Squeezenet (unfinished)
           
        - Sjetbot training
            - Original training and training based on selected date when initializing Sjetbot from GUI
    
    

"""


class ClassificationModel():
    # initializes the classification model selected in GUI 
    # options are: CNN own design, CNN mobile net transfer learning, CNN paper (unfinished), CNN Squeezenet (unfinished)
    def __init__(self, model):
        self.model = model

    def get_applebatch_classification(batch_id):
            

class Applebatch():
    # This class creates objects that can be used to examine and test the other classes in this program
    def __init__(self, apple_directory):
        self.apple_directory = apple_directory
        self.batch_size = 80
        self.batch_images = []
        self.batch_ID = # names the batch with the current date and time
        for file in apple_directory:
            if len(self.batch_images) < 80:
                # fills self.batchImages with randomly selected apples untill it has 80 apples
                random_apple = apple_directory[randint[len(apple_directory)]]
            else:
                break
        return batch_images
    
    
    # returns the aql of the batch
    def get_aql(self):

        





if __name__ == __main__
    main()