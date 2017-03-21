import django
django.setup()
from prospects.models import Question
from prospects.models import Choice
from django.shortcuts import get_object_or_404, render
from django.test.client import RequestFactory

def ch_main():
    rf = RequestFactory()
    request = rf.post('/submit/', {'foo': 'bar'})
    #tst = get_object_or_404(Question, pk=1)
    #print 'Question tst 1'
    #print tst
    #print tst.question_text
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    print latest_question_list
    context = { 'latest_question_list': latest_question_list }
    ret = render(request, 'prospects/index.html', context)
    print ret
    #for question in latest_question_list:
    #    print question

    #ch=Choice.objects.all()
    #print ch
    #for choice in question.choice_set.all():
    #    print choice
    '''
    colNames = Chance._meta.get_fields()
    colNameList=[item.name for item in colNames]
    valList=Chance.objects.values_list()
    valNamesList=[item for item in valList]
    colCount = 0
    collectList = []
    displayList = []
    for colName in colNameList:
        if colCount !=0:
            displayList.append(colName)
        colCount +=1
    collectList.append(displayList)
    displayList = []
    for item in valNamesList:
        valNamesCount=0
        for subItem in item:
            if valNamesCount !=0:
                displayList.append(subItem)
            valNamesCount+=1
        collectList.append(displayList)
        displayList = []
    print ''
    print 'collectList'
    print ''
    for item in collectList:
        for subItem in item:
            print subItem,
        print ''
    #print colNamesList
    colDlsplayList = []
    for item in colNamesList:
        if item != 'id':
            colDlsplayList.append(item)

    dItems = []
    for item in val_list:
        dLine = []
        for subItem in item:
          if type(subItem) != int:
            dLine.append(subItem)
          #print 'dLine'
          #print dLine
        #print ''
        colDlsplayList.append(dLine)
    #print 'colDlsplayList'
    #print colDlsplayList
    
    for cText in colDlsplayList:
        print cText,
    '''

def main():
    ch_main()

if __name__ == "__main__": main()
