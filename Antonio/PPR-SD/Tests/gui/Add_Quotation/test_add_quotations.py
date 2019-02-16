from util.testbase import Testbase
import pytest

class Test_AddQuote(Testbase):
    

    @pytest.mark.SMOKE
    def test_add_construction_quotation(self,construction_quote_obj):
        construction_quote_obj.add_construction_quote()
     
