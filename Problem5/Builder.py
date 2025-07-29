class Report:
    def __init__(self):
        self.title = None
        self.toc = None
        self.data = None
        self.chart = None
        self.appendix = None

    def __str__(self):
        return f"Report(\
        title={self.title},\
        has_toc={self.toc},\
        has_data={self.data},\
        has_chart={self.chart},\
        has_appendix={self.appendix})" 

class ReportBuilder():
    
    def __init__(self):
        self.report = Report()

    def title(self, title : str):
        self.report.title = title
        return self

    def add_toc(self, toc: bool =True):
        self.report.toc = toc
        return self
    
    def add_data(self, data: bool =True):
        self.report.data = data
        return self
    
    def add_chart(self, chart: bool=True):
        self.report.chart = chart
        return self
    
    def add_appendix(self, appendix: bool =True):
        self.report.appendix = appendix
        return self.report

    def build(self):
        return self.report
    
    

report = (ReportBuilder().title("Annual Report 2023")
    .add_toc(True)
    .add_data(True)
    .build()
    )

report2 = (ReportBuilder().title("Monthly Report")
    .add_toc(False)
    .add_data(True)
    .add_chart(True)
    .add_appendix(False)
) 

print(report)  
print(report2)


"""it  hides the complexity of the Report constructor with many optional parameters
    It also ensures adding new optional methods won't affect existing calls."""