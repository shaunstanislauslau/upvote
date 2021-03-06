# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Monitoring metrics for the binary_health services."""

from upvote.gae.shared.common import monitoring
from upvote.monitoring import metrics


virustotal_requests = monitoring.SuccessFailureCounter(
    metrics.BINARY_HEALTH.VIRUSTOTAL_REQUESTS)

virustotal_new_lookups = monitoring.Counter(
    metrics.BINARY_HEALTH.VIRUSTOTAL_NEW_LOOKUPS, fields=[(u'state', str)])
