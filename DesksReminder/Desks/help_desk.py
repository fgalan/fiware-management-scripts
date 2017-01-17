__author__ = 'Manuel Escriche'

from datetime import date, datetime
from Basics.dataFinder import Data
from Basics.nickNames import ContactBook

class TechHelpDesk:
    def __init__(self):
        self.contactBook = ContactBook()

    def open(self):
        messages = list()
        for issue in Data().getTechHelpDeskOpen():
            created = datetime.strptime(issue.fields.created[:10], '%Y-%m-%d').date()
            unanswered = (date.today() - created).days
            if unanswered <= 1: continue
            summary = issue.fields.summary
            displayName = issue.fields.assignee.displayName.strip()
            nickName = self.contactBook.getNickName(displayName)
            emailAddress = issue.fields.assignee.emailAddress

            #status = issue.fields.status.name
            url = 'http://jira.fiware.org/browse/{}'.format(issue)
            subject = 'FIWARE: Help Desk - Tech Channel : Open Issue'

            message = 'Dear {},'.format(nickName.encode('utf-8')) +\
                "\n\nI noticed issue {} is still OPEN, i.e. not replied for {} days.".format(issue, unanswered) +\
                "\nLet me remind you of our rule to reply in the first 24 hours during working days." +\
                "\nI would appreciate you spent a minute to reply to this request and to evolve its status." +\
                "\n\nIssue Summary: {}".format(summary.encode('utf-8')) +\
                "\nYou can access it at {}".format(url) +\
                "\n\nIssues in the Help Desk - Tech Channel are available at\n\thttp://backlog.fiware.org/helpdesk/tech" +\
                '\n\nThanks in advance for cooperation!!' +\
                '\n\nKind Regards,' +\
                '\nFernando'
            messages.append(dict(issue=issue, summary=summary.encode('utf-8'),
                                 email=emailAddress, nickname=nickName.encode('utf-8'), displayname=displayName,
                                 subject=subject, body=message))
        return messages

    def inProgress(self):
        messages = list()
        for issue in Data().getTechHelpDeskInProgress():
            updated = datetime.strptime(issue.fields.updated[:10], '%Y-%m-%d').date()
            noupdated = (date.today() - updated).days
            if noupdated < 7: continue
            summary = issue.fields.summary
            displayName = issue.fields.assignee.displayName.strip()
            nickName = self.contactBook.getNickName(displayName)
            emailAddress = issue.fields.assignee.emailAddress

            url = 'http://jira.fiware.org/browse/{}'.format(issue)
            subject = 'FIWARE: Help Desk - Tech Channel : stalled Issue?'

            message = 'Dear {},'.format(nickName.encode('utf-8')) +\
                "\n\nI noticed issue {} is In Progress but no update happened in the last {} days.".format(issue, noupdated) +\
                "\nI would appreciate you spent a minute to update it by reporting its progress in a comment" \
                "\n\tor if there were a blocking condition, please, report it in a comment and evolve its status to Impeded." +\
                "\n\tor if it was answered, please, evolve its status." +\
                "\n\nIssue Summary: {}".format(summary.encode('utf-8')) +\
                "\nYou can access it at {}".format(url) +\
                "\n\nIssues in the Help Desk - Tech Channel are available at\n\thttp://backlog.fiware.org/helpdesk/tech" +\
                '\n\nThanks in advance for cooperation!!' +\
                '\n\nKind Regards,' +\
                '\nFernando'
            messages.append(dict(issue=issue, summary=summary.encode('utf-8'),
                                 email=emailAddress, nickname=nickName.encode('utf-8'), displayname=displayName,
                                 subject=subject, body=message))
        return messages

    def answered(self):
        messages = list()
        for issue in Data().getTechHelpDeskAnswered():
            updated = datetime.strptime(issue.fields.updated[:10], '%Y-%m-%d').date()
            noupdated = (date.today() - updated).days
            if noupdated < 4: continue
            summary = issue.fields.summary
            displayName = issue.fields.assignee.displayName.strip()
            nickName = self.contactBook.getNickName(displayName)
            emailAddress = issue.fields.assignee.emailAddress

            url = 'http://jira.fiware.org/browse/{}'.format(issue)
            subject = 'FIWARE: Help Desk - Tech Channel : Closed Issue?'

            message = 'Dear {},'.format(nickName.encode('utf-8')) +\
                "\n\nI noticed issue {} has been Answered but no update happened in the last {} days.".format(issue, noupdated) +\
                "\nI would appreciate you spent a minute to close it" \
                "\n\tor if the exchange continues, please, update its progress in a comment" \
                "\n\tor if there were a blocking condition, please, report it in a comment and evolve its status to Impeded." +\
                "\n\nIssue Summary: {}".format(summary.encode('utf-8')) +\
                "\nYou can access it at {}".format(url) +\
                "\n\nIssues in the Help Desk - Tech Channel are available at\n\thttp://backlog.fiware.org/helpdesk/tech" +\
                '\n\nThanks in advance for cooperation!!' +\
                '\n\nKind Regards,' +\
                '\nFernando'
            messages.append(dict(issue=issue, summary=summary.encode('utf-8'),
                                 email=emailAddress, nickname=nickName.encode('utf-8'), displayname=displayName,
                                 subject=subject, body=message))
        return messages

    def impeded(self):
        messages = list()
        for issue in Data().getTechHelpDeskImpeded():
            updated = datetime.strptime(issue.fields.updated[:10], '%Y-%m-%d').date()
            noupdated = (date.today() - updated).days
            if noupdated < 7: continue
            summary = issue.fields.summary
            displayName = issue.fields.assignee.displayName.strip()
            nickName = self.contactBook.getNickName(displayName)
            emailAddress = issue.fields.assignee.emailAddress

            url = 'http://jira.fiware.org/browse/{}'.format(issue)
            subject = 'FIWARE: Help Desk - Tech Channel : Impeded Issue?'

            message = 'Dear {},'.format(nickName.encode('utf-8')) +\
                "\n\nI noticed issue {} is Impeded but no update happened in the last {} days.".format(issue, noupdated) +\
                "\nI would appreciate you spent a minute to check its blocking condition persist:" \
                "\n\tif so, please, add a comment stating it" \
                "\n\tif not, please, get it back to In Progress, and address it" +\
                "\n\nIssue Summary: {}".format(summary.encode('utf-8')) +\
                "\nYou can access it at {}".format(url) +\
                "\n\nIssues in the Help Desk - Tech Channel are available at\n\thttp://backlog.fiware.org/helpdesk/tech" +\
                '\n\nThanks in advance for cooperation!!' +\
                '\n\nKind Regards,' +\
                '\nFernando'
            messages.append(dict(issue=issue, summary=summary.encode('utf-8'),
                                 email=emailAddress, nickname=nickName.encode('utf-8'), displayname=displayName,
                                 subject=subject, body=message))
        return messages

class LabHelpDesk:
    def __init__(self):
        self.contactBook = ContactBook()

    def open(self):
        messages = list()
        for issue in Data().getLabHelpDeskOpen():
            created = datetime.strptime(issue.fields.created[:10], '%Y-%m-%d').date()
            unanswered = (date.today() - created).days
            if unanswered <= 1: continue
            summary = issue.fields.summary
            displayName = issue.fields.assignee.displayName.strip()
            nickName = self.contactBook.getNickName(displayName)
            emailAddress = issue.fields.assignee.emailAddress

            url = 'http://jira.fiware.org/browse/{}'.format(issue)
            subject = 'FIWARE: Help Desk - Lab Channel : Open Issue'

            message = 'Dear {},'.format(nickName.encode('utf-8')) +\
                "\n\nI noticed issue {} is still OPEN, i.e. not replied for {} days.".format(issue, unanswered) +\
                "\nLet me remind you of our rule to reply in the first 24 hours during working days." +\
                "\nI would appreciate you spent a minute to reply to this request and to evolve its status." +\
                "\n\nIssue Summary: {}".format(summary.encode('utf-8')) +\
                "\nYou can access it at {}".format(url) +\
                "\n\nIssues in the Help Desk - Lab Channel are available at\n\thttp://backlog.fiware.org/helpdesk/lab" +\
                '\n\nThanks in advance for cooperation!!' +\
                '\n\nKind Regards,' +\
                '\nFernando'
            messages.append(dict(issue=issue, summary=summary.encode('utf-8'),
                                 email=emailAddress, nickname=nickName.encode('utf-8'), displayname=displayName,
                                 subject=subject, body=message))
        return messages

    def inProgress(self):
        messages = list()
        for issue in Data().getLabHelpDeskInProgress():
            updated = datetime.strptime(issue.fields.updated[:10], '%Y-%m-%d').date()
            noupdated = (date.today() - updated).days
            if noupdated < 7: continue
            summary = issue.fields.summary
            displayName = issue.fields.assignee.displayName.strip()
            nickName = self.contactBook.getNickName(displayName)
            emailAddress = issue.fields.assignee.emailAddress

            url = 'http://jira.fiware.org/browse/{}'.format(issue)
            subject = 'FIWARE: Help Desk - Lab Channel : stalled Issue?'

            message = 'Dear {},'.format(nickName.encode('utf-8')) +\
                "\n\nI noticed issue {} is In Progress but no update happened in the last {} days.".format(issue, noupdated) +\
                "\nI would appreciate you spent a minute to update it by reporting its progress in a comment" \
                "\n\tor if there were a blocking condition, please, report it in a comment and evolve its status to Impeded." +\
                "\n\tor if it was answered, please, progress its status." +\
                "\n\nIssue Summary: {}".format(summary.encode('utf-8')) +\
                "\nYou can access it at {}".format(url) +\
                "\n\nIssues in the Help Desk - Lab Channel are available at\n\thttp://backlog.fiware.org/helpdesk/lab" +\
                '\n\nThanks in advance for cooperation!!' +\
                '\n\nKind Regards,' +\
                '\nFernando'
            messages.append(dict(issue=issue, summary=summary.encode('utf-8'),
                                 email=emailAddress, nickname=nickName.encode('utf-8'), displayname=displayName,
                                 subject=subject, body=message))
        return messages

    def answered(self):
        messages = list()
        for issue in Data().getLabHelpDeskAnswered():
            updated = datetime.strptime(issue.fields.updated[:10], '%Y-%m-%d').date()
            noupdated = (date.today() - updated).days
            if noupdated < 4: continue
            summary = issue.fields.summary
            displayName = issue.fields.assignee.displayName.strip()
            nickName = self.contactBook.getNickName(displayName)
            emailAddress = issue.fields.assignee.emailAddress

            #status = issue.fields.status.name
            url = 'http://jira.fiware.org/browse/{}'.format(issue)
            subject = 'FIWARE: Help Desk - Lab Channel : Closed Issue?'

            message = 'Dear {},'.format(nickName.encode('utf-8')) +\
                "\n\nI noticed issue {} has been Answered but no update happened in the last {} days.".format(issue, noupdated) +\
                "\nI would appreciate you spent a minute to close it" \
                "\n\tor if the exchange continues, please, update its progress in a comment" \
                "\n\tor if there were a blocking condition, please, report it in a comment and evolve its status to Impeded." +\
                "\n\nIssue Summary: {}".format(summary.encode('utf-8')) +\
                "\nYou can access it at {}".format(url) +\
                "\n\nIssues in the Help Desk - Lab Channel are available at\n\thttp://backlog.fiware.org/helpdesk/lab" +\
                '\n\nThanks in advance for cooperation!!' +\
                '\n\nKind Regards,' +\
                '\nFernando'
            messages.append(dict(issue=issue, summary=summary.encode('utf-8'),
                                 email=emailAddress, nickname=nickName.encode('utf-8'), displayname=displayName,
                                 subject=subject, body=message))
        return messages

    def impeded(self):
        messages = list()
        for issue in Data().getLabHelpDeskImpeded():
            updated = datetime.strptime(issue.fields.updated[:10], '%Y-%m-%d').date()
            noupdated = (date.today() - updated).days
            if noupdated < 7: continue
            summary = issue.fields.summary
            displayName = issue.fields.assignee.displayName.strip()
            nickName = self.contactBook.getNickName(displayName)
            emailAddress = issue.fields.assignee.emailAddress

            url = 'http://jira.fiware.org/browse/{}'.format(issue)
            subject = 'FIWARE: Help Desk - Lab Channel : Impeded Issue?'

            message = 'Dear {},'.format(nickName.encode('utf-8')) +\
                "\n\nI noticed issue {} is Impeded but no update happened in the last {} days.".format(issue, noupdated) +\
                "\nI would appreciate you spent a minute to check its blocking condition persist:" \
                "\n\tif so, please, add a comment stating it" \
                "\n\tif not, please, get it back to In Progress, and address it" +\
                "\n\nIssue Summary: {}".format(summary.encode('utf-8')) +\
                "\nYou can access it at {}".format(url) +\
                "\n\nIssues in the Help Desk - Lab Channel are available at\n\thttp://backlog.fiware.org/helpdesk/lab" +\
                '\n\nThanks in advance for cooperation!!' +\
                '\n\nKind Regards,' +\
                '\nFernando'
            messages.append(dict(issue=issue, summary=summary.encode('utf-8'),
                                 email=emailAddress, nickname=nickName.encode('utf-8'), displayname=displayName,
                                 subject=subject, body=message))
        return messages



class OthersHelpDesk:
    def __init__(self):
        self.contactBook = ContactBook()
        self.channels = {'FIWARE-COLLABORATION-REQ':'Collaboration',
                         'FIWARE-FEEDBACK':'Feedback',
                         'FIWARE-GENERAL-HELP':'General',
                         'FIWARE-MUNDUS-REQ':'Mundus',
                         'FIWARE-OPEN-DATA-REQ':'OpenData',
                         'FIWARE-OPS-HELP':'Operations',
                         'FIWARE-SMART-CITIES-REQ':'SmartCities',
                         'FIWARE-SPEAKERS-REQ':'Speakers',
                         'FIWARE-TRAINING-REQ':'Training'}

    def open(self):
        messages = list()
        for issue in Data().getOthersHelpDeskOpen():
            created = datetime.strptime(issue.fields.created[:10], '%Y-%m-%d').date()
            unanswered = (date.today() - created).days
            if unanswered <= 1: continue
            summary = issue.fields.summary
            displayName = issue.fields.assignee.displayName.strip()
            nickName = self.contactBook.getNickName(displayName)
            emailAddress = issue.fields.assignee.emailAddress
            channel = self.channels[issue.fields.components[0].name]

            #status = issue.fields.status.name
            url = 'http://jira.fiware.org/browse/{}'.format(issue)
            subject = 'FIWARE: Help Desk - {} Channel : Open Issue'.format(channel)

            message = 'Dear {},'.format(nickName.encode('utf-8')) +\
                "\n\nI noticed issue {} is still OPEN, i.e. not replied for {} days.".format(issue, unanswered) +\
                "\nLet me remind you of our rule to reply in the first 24 hours during working days." +\
                "\nI would appreciate you spent a minute to reply to this request and to evolve its status." +\
                "\n\nIssue Summary: {}".format(summary.encode('utf-8')) +\
                "\nYou can access it at {}".format(url) +\
                "\n\nIssues in the Help Desk - {0} Channel are available at\n\thttp://backlog.fiware.org/helpdesk/channel/{0}".format(channel) +\
                '\n\nThanks in advance for cooperation!!' +\
                '\n\nKind Regards,' +\
                '\nFernando'
            messages.append(dict(issue=issue, summary=summary.encode('utf-8'),
                                 email=emailAddress, nickname=nickName.encode('utf-8'), displayname=displayName,
                                 subject=subject, body=message))
        return messages

    def inProgress(self):
        messages = list()
        for issue in Data().getOthersHelpDeskInProgress():
            updated = datetime.strptime(issue.fields.updated[:10], '%Y-%m-%d').date()
            noupdated = (date.today() - updated).days
            if noupdated < 7: continue
            summary = issue.fields.summary
            displayName = issue.fields.assignee.displayName.strip()
            nickName = self.contactBook.getNickName(displayName)
            emailAddress = issue.fields.assignee.emailAddress
            channel = self.channels[issue.fields.components[0].name]

            url = 'http://jira.fiware.org/browse/{}'.format(issue)
            subject = 'FIWARE: Help Desk - {} Channel : stalled Issue?'.format(channel)

            message = 'Dear {},'.format(nickName.encode('utf-8')) +\
                "\n\nI noticed issue {} is In Progress but no update happened in the last {} days.".format(issue, noupdated) +\
                "\nI would appreciate you spent a minute to update it by reporting its progress in a comment" \
                "\n\tor if there were a blocking condition, please, report it in a comment and evolve its status to Impeded." +\
                "\n\tor if it was answered, please, evolve its status." +\
                "\n\nIssue Summary: {}".format(summary.encode('utf-8')) +\
                "\nYou can access it at {}".format(url) +\
                "\n\nIssues in the Help Desk - {0} Channel are available at\n\thttp://backlog.fiware.org/helpdesk/channel/{0}".format(channel) +\
                '\n\nThanks in advance for cooperation!!' +\
                '\n\nKind Regards,' +\
                '\nFernando'
            messages.append(dict(issue=issue, summary=summary.encode('utf-8'),
                                 email=emailAddress, nickname=nickName.encode('utf-8'), displayname=displayName,
                                 subject=subject, body=message))
        return messages

    def answered(self):
        messages = list()
        for issue in Data().getOthersHelpDeskAnswered():
            updated = datetime.strptime(issue.fields.updated[:10], '%Y-%m-%d').date()
            noupdated = (date.today() - updated).days
            if noupdated < 4: continue
            summary = issue.fields.summary
            displayName = issue.fields.assignee.displayName.strip()
            nickName = self.contactBook.getNickName(displayName)
            emailAddress = issue.fields.assignee.emailAddress
            channel = self.channels[issue.fields.components[0].name]

            url = 'http://jira.fiware.org/browse/{}'.format(issue)
            subject = 'FIWARE: Help Desk - {} Channel : Closed Issue?'.format(channel)

            message = 'Dear {},'.format(nickName.encode('utf-8')) +\
                "\n\nI noticed issue {} has been Answered but no update happened in the last {} days.".format(issue, noupdated) +\
                "\nI would appreciate you spent a minute to close it" \
                "\n\tor if the exchange continues, please, update its progress in a comment" \
                "\n\tor if there were a blocking condition, please, report it in a comment and evolve its status to Impeded." +\
                "\n\nIssue Summary: {}".format(summary.encode('utf-8')) +\
                "\nYou can access it at {}".format(url) +\
                "\n\nIssues in the Help Desk - {0} Channel are available at\n\thttp://backlog.fiware.org/helpdesk/channel/{0}".format(channel) +\
                '\n\nThanks in advance for cooperation!!' +\
                '\n\nKind Regards,' +\
                '\nFernando'
            messages.append(dict(issue=issue, summary=summary.encode('utf-8'),
                                 email=emailAddress, nickname=nickName.encode('utf-8'), displayname=displayName,
                                 subject=subject, body=message))
        return messages

    def impeded(self):
        messages = list()
        for issue in Data().getOthersHelpDeskImpeded():
            updated = datetime.strptime(issue.fields.updated[:10], '%Y-%m-%d').date()
            noupdated = (date.today() - updated).days
            if noupdated < 7: continue
            summary = issue.fields.summary
            displayName = issue.fields.assignee.displayName.strip()
            nickName = self.contactBook.getNickName(displayName)
            emailAddress = issue.fields.assignee.emailAddress
            channel = self.channels[issue.fields.components[0].name]

            url = 'http://jira.fiware.org/browse/{}'.format(issue)
            subject = 'FIWARE: Help Desk - {} Channel : Impeded Issue?'.format(channel)

            message = 'Dear {},'.format(nickName.encode('utf-8')) +\
                "\n\nI noticed issue {} is Impeded but no update happened in the last {} days.".format(issue, noupdated) +\
                "\nI would appreciate you spent a minute to check its blocking condition persist:" \
                "\n\tif so, please, add a comment stating it" \
                "\n\tif not, please, get it back to In Progress, and address it" +\
                "\n\nIssue Summary: {}".format(summary.encode('utf-8')) +\
                "\nYou can access it at {}".format(url) +\
                "\n\nIssues in the Help Desk - {0} Channel are available at\n\thttp://backlog.fiware.org/helpdesk/channel/{0}".format(channel) +\
                '\n\nThanks in advance for cooperation!!' +\
                '\n\nKind Regards,' +\
                '\nFernando'
            messages.append(dict(issue=issue, summary=summary.encode('utf-8'),
                                 email=emailAddress, nickname=nickName.encode('utf-8'), displayname=displayName,
                                 subject=subject, body=message))
        return messages


if __name__ == "__main__":
    pass
