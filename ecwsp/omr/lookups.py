from django.db.models import Q
from ecwsp.benchmarks.models import Benchmark
from ecwsp.omr.models import Test
from ajax_select import LookupChannel

class BenchmarkLookup(LookupChannel):
    model = Benchmark
    
    def get_query(self,q,request):
        result = Benchmark.objects.all()
        if request.session['omr_test_id']:
            test = Test.objects.get(id=request.session['omr_test_id'])
            if test.department:
                result = result.filter(measurement_topics__department=test.department)
        result = result.filter(Q(name__icontains=q) | Q(number__icontains=q))
        return result

    def get_objects(self,ids):
        return Benchmark.objects.filter(pk__in=ids).order_by('name')