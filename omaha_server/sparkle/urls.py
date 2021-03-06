# coding: utf8

"""
This software is licensed under the Apache 2 license, quoted below.

Copyright 2014 Crystalnix Limited

Licensed under the Apache License, Version 2.0 (the "License"); you may not
use this file except in compliance with the License. You may obtain a copy of
the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations under
the License.
"""

from django.conf.urls import patterns, url

from views import SparkleView


urlpatterns = patterns('',
    url(r'^(?P<app_name>[\w-]+)/(?P<channel>[\w-]+)/appcast.xml$',
        SparkleView.as_view(), name='sparkle_appcast'),
)
