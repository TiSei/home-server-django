from views.TemplateView import StandardTemplateView
from django.core.paginator import Paginator

class StandardTemplateListView(StandardTemplateView):
    template_name='standard_list_layout.html'
    @staticmethod
    def build_config(
        title, new_url, data, object_template, 
        two_cols = True, action_url = None,
        has_filter = False, page_size = -1):
        attrs = {
            'title':title,
            'new_url':new_url,
            'data':data,
            'object_template':object_template,
            'filter':has_filter,
            'page_size':page_size,
        }
        if two_cols:
            attrs['two_cols'] = True
        if action_url:
            attrs['action_url'] = action_url
        return attrs
    def get_configs(self):
        return []
    def apply_filter(self, queryset):
        return None, None, {}
    def apply_paging(self, queryset, page_size):
        page_number = self.request.GET.get(f'page', 1)
        paginator = Paginator(queryset, page_size or 10)
        return paginator.get_page(page_number)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query_params = self.request.GET.copy()
        if 'page' in query_params:
            query_params.pop('page')
        context['current_query'] = query_params.urlencode()
        configs = self.get_configs()
        if (len(configs) == 1):
            cfg = configs[0]
            qs = cfg.pop('data')
            if (cfg['filter']):
                qs, cfg['filter_template'], cfg['filter_values'] = self.apply_filter(qs)
                context['Website']['Sidebar'] = True
            if (cfg['page_size']>0):
                page_obj = self.apply_paging(qs, cfg['page_size'])
                cfg['objects'] = page_obj
            else:
                cfg['objects'] = qs
            context['lists'] = [cfg]
        else:
            lists = []
            for idx, cfg in enumerate(configs):
                cfg['objects'] = cfg.pop('data')
                lists.append(cfg)
            context['lists'] = lists
        return context