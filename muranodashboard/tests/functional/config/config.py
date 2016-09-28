#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os
from oslo_config import cfg

murano_group = cfg.OptGroup(name='murano', title="murano configs")

MuranoGroup = [
    cfg.StrOpt('horizon_url',
               default='http://127.0.0.1/horizon',
               help="murano dashboard url"),
    cfg.StrOpt('user',
               default='admin',
               help="keystone user"),
    cfg.StrOpt('password',
               default='pass',
               help="password for keystone user"),
    cfg.StrOpt('tenant',
               default='admin',
               help='keystone tenant'),
    cfg.StrOpt('keystone_url',
               default='http://localhost:5000/v2.0/',
               help='keystone url'),
    cfg.StrOpt('murano_url',
               default='http://127.0.0.1:8082',
               help='murano url'),
    cfg.IntOpt('items_per_page',
               default=20,
               help='items per page displayed'),
    cfg.StrOpt('packages_service',
               default='murano',
               help='murano packages service, either "murano" or "glare"'),
]


def register_config(config, config_group, config_opts):

    config.register_group(config_group)
    config.register_opts(config_opts, config_group)

path = os.path.join(os.path.dirname(__file__), "config.conf")

if os.path.exists(path):
    cfg.CONF([], project='muranodashboard', default_config_files=[path])

register_config(cfg.CONF, murano_group, MuranoGroup)

common = cfg.CONF.murano
