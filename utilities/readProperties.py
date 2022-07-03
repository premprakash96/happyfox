import configparser

config = configparser.RawConfigParser()
config.read('.\\Configurations\\config.ini')


class ReadConfig:
    @staticmethod
    def getAgentUrl():
        url = config.get('common info', 'agentUrl')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getTicketUrl():
        ticket_url = config.get('common info', 'ticketUrl')
        return ticket_url

    @staticmethod
    def getPriorityName():
        priority_name = config.get('priority info', 'name')
        return priority_name

    @staticmethod
    def getPriorityDescription():
        priority_desc = config.get('priority info', 'description')
        return priority_desc

    @staticmethod
    def getPriorityReplace():
        delete_replace = config.get('priority info', 'replacePriority')
        return delete_replace

    @staticmethod
    def getStatusName():
        status_name = config.get('status info', 'name')
        return status_name

    @staticmethod
    def getStatusDescription():
        status_desc = config.get('status info', 'description')
        return status_desc

    @staticmethod
    def getStatusBehaviour():
        status_behaviour = config.get('status info', 'behaviour')
        return status_behaviour

    @staticmethod
    def getStatusReplace():
        delete_replace = config.get('status info', 'replaceStatus')
        return delete_replace

    @staticmethod
    def getIssueSubject():
        issue_subject = config.get('issue info', 'subject')
        return issue_subject

    @staticmethod
    def getIssueMessage():
        issue_message = config.get('issue info', 'message')
        return issue_message

    @staticmethod
    def getIssueAttachment():
        issue_attachment = config.get('issue info', 'attachment')
        return issue_attachment

    @staticmethod
    def getIssueFullName():
        issue_full_name = config.get('issue info', 'fullname')
        return issue_full_name

    @staticmethod
    def getIssueEmail():
        issue_email = config.get('issue info', 'email')
        return issue_email

    @staticmethod
    def getIssueReplyCannedAction():
        issue_canned_action = config.get('issue reply info', 'cannedAction')
        return issue_canned_action

    @staticmethod
    def getIssueReplyStatus():
        issue_reply_status = config.get('issue reply info', 'status')
        return issue_reply_status

    @staticmethod
    def getIssueReplyPriority():
        issue_reply_priority = config.get('issue reply info', 'priority')
        return issue_reply_priority

    @staticmethod
    def getIssueReplyTags():
        issue_reply_tags = config.get('issue reply info', 'tags')
        return issue_reply_tags
