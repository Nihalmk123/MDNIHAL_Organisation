import json


class Commenlib:
    def __init__(self):
        self.DEFAULT_REDIRECT_PATH={'ROOT':'/'}
        self.TOAST_ERROR = 'error'
        self.TOAST_WARNING = 'warning'
        self.TOAST_SUCCESS = 'success'
        self.TOAST_SUCCESS_MSG = 'Record Updated Successfully!'
        self.TOAST_VOTER_COUNT_ERROR_MSG = 'Voter Count Mismatch!!'
        self.TOAST_ERROR_MSG = 'Failed to Update Records!'
        self.TOAST_RECORD_EXISTS_MSG = 'Record Already Exists!'
        self.TOAST_ACTIVATION_SUCCESS_MSG = 'Activated Client'
        self.TOAST_DEACTIVATION_SUCCESS_MSG = 'Deactivated Client'
        self.TOAST_ACTIVATION_ERROR_MSG = 'Failed to Activate Client'
        self.TOAST_DEACTIVATION_ERROR_MSG = 'Failed to Deactivate Client'






# import pdfcrowd

class CommonLib:
    def __init__(self):
        self.PROJECT_NAME = 'demo'
        self.DEFAULT_REDIRECT_PATH = {'ROOT': '/'}

        self.MEDIA_PATH_CHOICES = {
            'society': "organization/society_image/",
            'institute': "organization/institute_image/",
            'office': "organization/office_image/",

        }

    def fetch_common_info(self, request):
        """
        This method is used to fetch the common information of the users
        :param request:
        :return:
        """

        record_details = {'project_name': self.PROJECT_NAME,
                          'username': str(request.user),
                          }
        # 'role': str(user_details)}
        return json.loads(json.dumps(record_details))