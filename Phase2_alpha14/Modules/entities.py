import base64
eval(compile(base64.b64decode(b'aW1wb3J0IHBhcmFtZXRlcnMKaW1wb3J0IHJhbmRvbQoKZnJvbSB0eXBpbmcgaW1wb3J0IFR1cGxlLCBPcHRpb25hbAoKY2xhc3MgUGF0Y2g6CiAgIiIiCiAgQSBwYXRjaCBvZiBncmFzcyBhdCBhIGdpdmVuIHBhaXIgb2YgY29vcmRpbmF0ZXMuCiAgIiIiCiAgCiAgX19zbG90c19fID0gWwogICAgIl8wIiwKICAgICJfMSIsCiAgICAiXzIiLAogICAgIl8zIiwKICAgICJfNCIsCiAgXQogIAogIG1pbl9ncmFzc19ncm93dGggPSAxCiAgbWF4X2dyYXNzX2dyb3d0aCA9IDQKICBtYXhfZ3Jhc3NfYW1vdW50ID0gMzAKCiAgZGVmIF9faW5pdF9fKHNlbGYsIHggOiBpbnQsIHk6aW50KTogICAKICAgICIiIgogICAgICogYHhgOiB0aGUgd2VzdC1lYXN0IGNvcnJkaW5hdGUgZm9yIHRoaXMgcGF0Y2guCiAgICAgKiBgeWA6IHRoZSBub3J0aC1zb3V0aCBjb29yZGluYXRlIGZvciB0aGlzIHBhdGNoLgogICAgIiIiCiAgICBzZWxmLl8yID0gKHgseSkKICAgIHNlbGYuXzEgPSByYW5kb20ucmFuZHJhbmdlKHJvdW5kKFBhdGNoLm1heF9ncmFzc19hbW91bnQgKiAwLjMpLFBhdGNoLm1heF9ncmFzc19hbW91bnQpCiAgICBzZWxmLl8zID0gW10KICAgIHNlbGYuXzQgPSBbXQogICAgc2VsZi5fMCA9IFtdCiAgICBkZWYgZjAoaSk6CiAgICAgIHJldHVybiBzZWxmLl8wWyBpICUgMTNdCiAgICBzZWxmLl8wLmFwcGVuZChmMCkKICAgIGRlZiBmKHMpOgogICAgICBpZiBzLl8xIDwgUGF0Y2gubWF4X2dyYXNzX2Ftb3VudDoKICAgICAgICBnID0gcy5fMSArIHJhbmRvbS5yYW5kcmFuZ2UoUGF0Y2gubWluX2dyYXNzX2dyb3d0aCxQYXRjaC5tYXhfZ3Jhc3NfZ3Jvd3RoKQogICAgICAgIHMuXzEgPSBtaW4oZywgUGF0Y2gubWF4X2dyYXNzX2Ftb3VudCkKICAgIHNlbGYuXzAuYXBwZW5kKGYpCiAgICBkZWYgZihzKToKICAgICAgcmV0dXJuIHMuXzEKICAgIHNlbGYuXzAuYXBwZW5kKGYpCiAgICBkZWYgZihzKToKICAgICAgcmV0dXJuIHMuXzIKICAgIHNlbGYuXzAuYXBwZW5kKGYpCiAgICBkZWYgZihhKToKICAgICAgaWYgaXNpbnN0YW5jZShhLEZveCk6CiAgICAgICAgcmV0dXJuIHNlbGYuXzMgCiAgICAgIGVsc2U6CiAgICAgICAgcmV0dXJuIHNlbGYuXzQKICAgIHNlbGYuXzAuYXBwZW5kKGYpCiAgICBkZWYgZigpOgogICAgICBmb3IgYSBpbiBzZWxmLl8zOgogICAgICAgIGlmIGEuaXNfYWxpdmUoKToKICAgICAgICAgIHJldHVybiBUcnVlCiAgICAgIHJldHVybiBGYWxzZQogICAgc2VsZi5fMC5hcHBlbmQoZikKICAgIGRlZiBmKCk6CiAgICAgIGZvciBhIGluIHNlbGYuXzQ6CiAgICAgICAgaWYgYS5pc19hbGl2ZSgpOgogICAgICAgICAgcmV0dXJuIFRydWUKICAgICAgcmV0dXJuIEZhbHNlCiAgICBzZWxmLl8wLmFwcGVuZChmKQogICAgZGVmIGYoKToKICAgICAgZm9yIGEgaW4gc2VsZi5fNDoKICAgICAgICBpZiBhLmlzX2FsaXZlKCk6CiAgICAgICAgICByZXR1cm4gYQogICAgICByZXR1cm4gTm9uZQogICAgc2VsZi5fMC5hcHBlbmQoZikKICAgIGRlZiBmKCk6CiAgICAgIHJldHVybiBzZWxmLl80ICsgc2VsZi5fMwogICAgc2VsZi5fMC5hcHBlbmQoZikKICAgIHNlbGYuXzAuYXBwZW5kKHByaW50KQogICAgc2VsZi5fMC5hcHBlbmQoZjApCiAgICBzZWxmLl8wLmFwcGVuZChmKQogICAgc2VsZi5fMC5hcHBlbmQocm91bmQpCiAgICBzZWxmLl8wLmFwcGVuZChmMCkKICAgIAogIGRlZiB0aWNrKHNlbGYpOgogICAgIiIiCiAgICBSZWNvcmRzIHRoZSBwYXNzYWdlIG9mIHRpbWUgKG9uZSBzdGVwIGluIHRoZSBzaW11bGF0aW9uKS4gR3Jhc3MgZ3Jvd3MuCiAgICAiIiIKICAgIHNlbGYuXzBbMF0oMjcpKHNlbGYpCgogIGRlZiBncmFzcyhzZWxmKSAtPiBpbnQ6CiAgICAiIiIKICAgIFJldHVybnMgdGhlIGFtb3VudCBvZiBncmFzcyBpbiB0aGlzIHBhdGNoLgogICAgIiIiCiAgICByZXR1cm4gc2VsZi5fMFsxMF0oODApKHNlbGYpCgogIGRlZiBjb29yZGluYXRlcyhzZWxmKSAtPiBUdXBsZVtpbnQsaW50XToKICAgICIiIgogICAgUmV0dXJucyB0aGUgY29vcmRpbmF0ZXMgaW4gdGhlIHNpbXVsYXRlZCB3b3JsZCBmb3IgdGhpcyBwYXRjaC4KICAgICIiIgogICAgcmV0dXJuIHNlbGYuXzBbMTBdKDk0KShzZWxmKQoKICBkZWYgYWRkKHNlbGYsYW5pbWFsKToKICAgIGlmIGFuaW1hbC5pc19hbGl2ZSgpIGFuZCBhbmltYWwgbm90IGluIHNlbGYuXzBbMF0oMzAzKShhbmltYWwpOgogICAgICBzZWxmLl8wWzBdKDEyMSkoYW5pbWFsKS5hcHBlbmQoYW5pbWFsKQoKICBkZWYgcmVtb3ZlKHNlbGYsYW5pbWFsKToKICAgIHRyeTogc2VsZi5fMFswXSg5NzkpKGFuaW1hbCkucmVtb3ZlKGFuaW1hbCkKICAgIGV4Y2VwdCBWYWx1ZUVycm9yOiBwYXNzCgogIGRlZiBoYXNfYWxpdmVfZm94KHNlbGYpIC0+IGJvb2w6CiAgICByZXR1cm4gc2VsZi5fMFswXSg1NjQpKCkgCiAgICAKICBkZWYgaGFzX2FsaXZlX3JhYmJpdChzZWxmKSAtPiBib29sOgogICAgcmV0dXJuIHNlbGYuXzBbMF0oMzgzKSgpCgogIGRlZiBhbmltYWxzKHNlbGYpOgogICAgIiIiCiAgICBSZXR1cm5zIGEgbGlzdCBjb250YWluaW5nIHRoZSBhbmltYWxzIG9uIHRoZSBwYXRjaC4KICAgICIiIgogICAgcmV0dXJuIHNlbGYuXzBbMTBdKDExMikoKQogIAogIGRlZiBfX3JlcHJfXyhzZWxmKSAtPiBzdHI6CiAgICByZXR1cm4gZiJQYXRjaHtzZWxmLmNvb3JkaW5hdGVzKCl9IgoKICBkZWYgX19zdHJfXyhzZWxmKSAtPiBzdHI6CiAgICByZXR1cm4gZiIiIlBhdGNoOgogIGNvb3JkaW5hdGVzICAgICAgIHtzZWxmLmNvb3JkaW5hdGVzKCl9CiAgZ3Jhc3M6ICAgICAgICAgICAge3NlbGYuZ3Jhc3MoKX0KICBoYXMgYWxpdmUgZm94OiAgICB7c2VsZi5oYXNfYWxpdmVfZm94KCl9CiAgaGFzIGFsaXZlIHJhYmJpdDoge3NlbGYuaGFzX2FsaXZlX3JhYmJpdCgpfQoiIiIKCmNsYXNzIEFuaW1hbDoKICAiIiIKICBBIGdlbmVyaWMgYW5pbWFsIGluIHRoZSBzaW11bGF0aW9uLiBTZWUgY2xhc3NlcyBgRm94YCBhbmQgYFJhYmJpdGAuCiAgIiIiCgogIF9fc2xvdHNfXyA9IFsKICAgICJfMCIsCiAgICAiXzEiLAogICAgIl8yIiwKICAgICJfMyIsCiAgICAiXzQiCiAgICBdCgogIGRlZiBfX2luaXRfXyhzZWxmLCBwb3B1bGF0aW9uIDogcGFyYW1ldGVycy5Qb3B1bGF0aW9uLCAKICAgICAgICAgICAgICAgcGF0Y2ggOiBQYXRjaCwgZW5lcmd5IDogaW50LCBhZ2UgOiBpbnQpOgogICAgYXNzZXJ0IDAgPD0gYWdlIDw9IHBvcHVsYXRpb24ubWF4X2FnZQogICAgYXNzZXJ0IDAgPD0gZW5lcmd5IDw9IHBvcHVsYXRpb24ubWF4X2VuZXJneQogICAgc2VsZi5fMCA9IFtdCiAgICBzZWxmLl8xID0gcG9wdWxhdGlvbgogICAgc2VsZi5fMiA9IGVuZXJneQogICAgc2VsZi5fMyA9IGFnZQogICAgc2VsZi5fNCA9IHBhdGNoCiAgICBkZWYgZjAoaSk6IHJldHVybiBzZWxmLl8wWyBpICUgMTddCiAgICBzZWxmLl8wLmFwcGVuZChmMCkKICAgIGRlZiBmKHMpOiByZXR1cm4gcy5fMiA+IDAgYW5kIHMuXzMgPCBzLl8xLm1heF9hZ2UKICAgIHNlbGYuXzAuYXBwZW5kKGYpCiAgICBkZWYgZihzKTogcmV0dXJuIHMuXzQKICAgIHNlbGYuXzAuYXBwZW5kKGYpCiAgICBkZWYgZihzKTogcmV0dXJuIHMuXzMKICAgIHNlbGYuXzAuYXBwZW5kKGYpCiAgICBkZWYgZihzKTogcmV0dXJuIHMuXzIKICAgIHNlbGYuXzAuYXBwZW5kKGYpCiAgICBzZWxmLl8wLmFwcGVuZChtYXgpCiAgICBkZWYgZihzKToKICAgICAgaWYgcy5fMFswXSgxNDgwKShzKToKICAgICAgICBzLl8yID0gcy5fMFswXSg0NjQpKDAscy5fMiAtIHMuXzEubWV0YWJvbGlzbSkKICAgICAgICBzLl8zICs9IDEKICAgICAgICBpZiBub3Qgcy5fMFswXSg0NjApKHMpOiBzLl80LnJlbW92ZShzKQogICAgc2VsZi5fMC5hcHBlbmQoZikKICAgIHNlbGYuXzAuYXBwZW5kKHJhbmRvbS5yYW5kb20pCiAgICBkZWYgZihzLGMscCk6CiAgICAgIGlmIHMuY2FuX3JlcHJvZHVjZSgpIGFuZCBcCiAgICAgICAgcy5fMFswXSg1MDApKCkgPCBzLl8xLnJlcHJvZHVjdGlvbl9wcm9iYWJpbGl0eToKICAgICAgICBzLl8yIC09IHMuXzBbMF0oNjcyKShzLl8xLnJlcHJvZHVjdGlvbl9taW5fZW5lcmd5ICogYy5yZXByb2R1Y3Rpb25fY29zdF9yYXRlKQogICAgICAgIHJldHVybiBjKHMuXzEsIHAsIDApCiAgICAgIGVsc2U6CiAgICAgICAgcmV0dXJuIE5vbmUKICAgIHNlbGYuXzAuYXBwZW5kKGYpCiAgICBzZWxmLl8wLmFwcGVuZChyb3VuZCkKICAgIGRlZiBmKHMscCk6CiAgICAgIHMuXzQucmVtb3ZlKHMpCiAgICAgIHMuXzQgPSBwCiAgICAgIHMuXzQuYWRkKHMpCiAgICBzZWxmLl8wLmFwcGVuZChmKQogICAgCgogIGRlZiBpc19hbGl2ZShzZWxmKSAtPiBib29sOgogICAgIiIiCiAgICBSZXR1cm5zIGBUcnVlYCBpZiB0aGUgYW5pbWFsIGlzIGFsaXZlLCBgRmFsc2VgIG90aGVyd2lzZS4KICAgICIiIgogICAgcmV0dXJuIHNlbGYuXzBbMF0oMTQ2Mykoc2VsZikKCiAgZGVmIHBhdGNoKHNlbGYpIC0+IFBhdGNoOgogICAgIiIiCiAgICBSZXR1cm5zIHRoZSBwb3NpdGlvbiBvZiB0aGUgYW5pbWFsLiBUaGUgdmFsdWUgZG9lcyBub3QgY2hhbmdlIGFmdGVyIHRoZSBkZWF0aCBvZiB0aGUgYW5pbWFsLiAKICAgICIiIgogICAgcmV0dXJuIHNlbGYuXzBbMF0oMTM2Mikoc2VsZikKCiAgZGVmIGFnZShzZWxmKSAtPiBpbnQ6CiAgICAiIiIKICAgIFJldHVybnMgdGhlIGFnZSBvZiB0aGUgYW5pbWFsLiBUaGUgdmFsdWUgZG9lcyBub3QgY2hhbmdlIGFmdGVyIHRoZSBkZWF0aCBvZiB0aGUgYW5pbWFsLiAKICAgICIiIgogICAgcmV0dXJuIHNlbGYuXzBbMF0oNDQ1KShzZWxmKQoKICBkZWYgZW5lcmd5KHNlbGYpIC0+IGludDoKICAgICIiIgogICAgUmV0dXJucyB0aGUgZW5lcmd5IG9mIHRoZSBhbmltYWwuIFRoZSB2YWx1ZSBkb2VzIG5vdCBjaGFuZ2UgYWZ0ZXIgdGhlIGRlYXRoIG9mIHRoZSBhbmltYWwuIAogICAgIiIiCiAgICByZXR1cm4gc2VsZi5fMFswXSg0ODApKHNlbGYpCgogIGRlZiBzYW1lX3NwZWNpZXNfaW4oc2VsZiwgcGF0Y2ggOiBQYXRjaCkgLT4gYm9vbDoKICAgICIiIgogICAgUmV0dXJuIGBUcnVlYCBpZiB0aGUgZ2l2ZW4gcGF0Y2ggY29udGFpbnMgYW4gYWxpdmUgYW5pbWFsIG9mIHRoZSBzYW1lIHNwZWNpZXMuCiAgICAiIiIKICAgIHBhc3MKCiAgZGVmIHByZWRhdG9yc19pbihzZWxmLCBwYXRjaCA6IFBhdGNoKSAtPiBib29sOgogICAgIiIiCiAgICBSZXR1cm5zIGBUcnVlYCBpZiB0aGUgZ2l2ZW4gcGF0Y2ggY29udGFpbnMgYSBhbGl2ZSBwcmVkYXRvciBvZiB0aGlzIGFuaW1hbC4KICAgICIiIgogICAgcGFzcwogIAogIGRlZiB0aWNrKHNlbGYpOgogICAgIiIiCiAgICBSZWNvcmRzIHRoZSBwYXNzYWdlIG9mIHRpbWUgKG9uZSBzdGVwIGluIHRoZSBzaW11bGF0aW9uKS4gSWYgdGhlIGFuaW1hbCBpcyBhbGl2ZSwgaXQgYWdlcyBhbmQgY29uc3VtZXMgaXRzIGVuZXJneS4gSWYgdGhlIGFuaW1hbCBiZWNvbWVzIHRvbyBvbGQgb3IgZGVwbGV0ZXMgaXRzIGVuZXJneSByZXNlcnZlLCBpdCBkaWVzIGFuZCBpdCBpcyByZW1vdmVkIGZyb20gaXRzIGN1cnJlbnQgcGF0Y2guCiAgICAiIiIKICAgIHJldHVybiBzZWxmLl8wWzBdKDQ2NSkoc2VsZikKCiAgZGVmIGZlZWQoc2VsZik6CiAgICAiIiIKICAgIEZlZWRzIGl0c2VsZiB1c2luZyB0aGUgcmVzb3VyY2VzIGF0IGl0cyBjdXJyZW50IGxvY2F0aW9uLgogICAgIiIiCiAgICByZXR1cm4gc2VsZi5fMFswXSg0MzYpKHNlbGYpCgogIGRlZiBjYW5fcmVwcm9kdWNlKHNlbGYpIC0+IGJvb2w6CiAgICAiIiIKICAgIFJldHVybnMgYFRydWVgIGlmIHRoZSBhbmltYWwgaXMgYWxpdmUsIGlzIG9sZCBlbm91Z2gsIGFuZCBoYXMgZW5vdWdoIGVuZXJneSB0byByZXByb2R1Y2UsIEZhbHNlIG90aGVyd2lzZS4KICAgICIiIgogICAgcmV0dXJuIHNlbGYuaXNfYWxpdmUoKSBhbmQgXAogICAgICBzZWxmLmVuZXJneSgpID49IHNlbGYuXzEucmVwcm9kdWN0aW9uX21pbl9lbmVyZ3kgYW5kIFwKICAgICAgc2VsZi5hZ2UoKSA+PSBzZWxmLl8xLnJlcHJvZHVjdGlvbl9taW5fYWdlCgogIGRlZiByZXByb2R1Y2Uoc2VsZiwgbmV3Ym9ybl9wYXRjaCA6IFBhdGNoKSAtPiBPcHRpb25hbFsnQW5pbWFsJ106CiAgICAiIiIKICAgIElmIHRoZSBhbmltYWwgaXMgYWxpdmUsIGl0IHRyaWVzIHRvIHJlcHJvZHVjZSB1c2luZyB0aGUgcGF0Y2ggcHJvdmlkZWQuCiAgICBSZXR1cm5zIGFuIGluc3RhbmNlIGZvciB0aGUgbmV3Ym9ybiAobG9jYXRlZCBhdCBgbmV3Ym9ybl9wYXRjaGApIG9yIE5vbmUuUGF0Y2hlcyBhcmUgdXBkYXRlZCBhY2NvcmRpbmdseS4KICAgICIiIgogICAgcmV0dXJuIE5vbmUKCiAgZGVmIF9yZXByb2R1Y2Uoc2VsZixzcGVjaWVzLHBhdGNoKToKICAgIHJldHVybiBzZWxmLl8wWzBdKDkyNikoc2VsZixzcGVjaWVzLHBhdGNoKQoKICBkZWYgbW92ZV90byhzZWxmLCBwYXRjaCA6IFBhdGNoKToKICAgICIiIgogICAgSWYgdGhlIGFuaW1hbCBpcyBhbGl2ZSwgaXQgZ29lcyBmcm9tIGl0cyBjdXJyZW50IHBhdGNoIHRvIHRoZSBnaXZlbiBvbmUuIFBhdGNoZXMgYXJlIHVwZGF0ZWQgYWNjb3JkaW5nbHkuCiAgICAiIiIKICAgIGFzc2VydCBzZWxmLmlzX2FsaXZlKCkKICAgIGFzc2VydCBzZWxmLnBhdGNoKCkgIT0gcGF0Y2gKICAgIGFzc2VydCBub3Qgc2VsZi5zYW1lX3NwZWNpZXNfaW4ocGF0Y2gpCiAgICByZXR1cm4gc2VsZi5fMFswXSg0MTgpKHNlbGYscGF0Y2gpCgpjbGFzcyBGb3goQW5pbWFsKToKICAiIiIKICBBIGZveCBpbiB0aGUgc2ltdWxhdGVkIHdvcmxkLiAKICAiIiIKCiAgZGVmIF9faW5pdF9fKHNlbGYsIHBvcHVsYXRpb24gOiBwYXJhbWV0ZXJzLlBvcHVsYXRpb24sIAogICAgICAgICAgICAgICBwYXRjaCA6IFBhdGNoLCBhZ2UgOiBpbnQpOiAgICAKICAgICIiIgogICAgICogYHBvcHVsYXRpb25gOiB0aGUgcGFyYW1ldGVycyBmb3IgdGhlIGZveCBwb3B1bGF0aW9uIHVzZWQgaW4gdGhpcyBydW4gb2YgdGhlIHNpbXVsYXRpb24uCiAgICAgKiBgcGF0Y2hgOiB0aGUgcG9zaXRpb24gYXNzaWduZWQgdG8gdGhpcyBhbmltYWwgKHRoZSBjb25zdHJ1Y3RvciB0YWtlcyBjYXJlIG9mIGFkZGluZyBpdCB0byB0aGUgbGlzdCBvZiBhbmltYWxzIG9mIHRoaXMgcGF0Y2gpLgogICAgICogYGFnZWA6IHRoZSBjdXJyZW50IGFnZSBvZiB0aGUgYW5pbWFsLgogICAgIiIiCiAgICBlbmVyZ3kgPSByb3VuZChwb3B1bGF0aW9uLm1heF9lbmVyZ3kgKiAwLjcpCiAgICBzdXBlcigpLl9faW5pdF9fKHBvcHVsYXRpb24scGF0Y2gsZW5lcmd5LGFnZSkKICAgIGRlZiBmKHMpOgogICAgICBpZiBzLmlzX2FsaXZlKCkgYW5kIFwKICAgICAgICBzLl8yIDwgcy5fMS5tYXhfZW5lcmd5IC0gMTA6CiAgICAgICAgciA9IHMuXzQuXzBbMF0oNjcwKSgpCiAgICAgICAgaWYgcjoKICAgICAgICAgIHIua2lsbCgpCiAgICAgICAgICBzLl8yID0gbWluKCBzLl8yICsgRm94LmZvb2RfZW5lcmd5X3Blcl91bml0LCAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcy5fMS5tYXhfZW5lcmd5KQogICAgc2VsZi5fMC5hcHBlbmQoZikKICAgIHNlbGYuXzQuYWRkKHNlbGYpCgogIGRlZiBzYW1lX3NwZWNpZXNfaW4oc2VsZiwgcGF0Y2ggOiBQYXRjaCkgLT4gYm9vbDoKICAgIHJldHVybiBwYXRjaC5fMFswXSg3MCkoKQoKICBkZWYgcHJlZGF0b3JzX2luKHNlbGYscGF0Y2ggOiBQYXRjaCkgLT4gYm9vbDoKICAgIHJldHVybiBGYWxzZQoKICByZXByb2R1Y3Rpb25fY29zdF9yYXRlID0gMC44NQoKICBkZWYgcmVwcm9kdWNlKHNlbGYsIG5ld2Jvcm5fcGF0Y2ggOiBQYXRjaCk6CiAgICByZXR1cm4gc2VsZi5fcmVwcm9kdWNlKEZveCxuZXdib3JuX3BhdGNoKQoKICBmb29kX2VuZXJneV9wZXJfdW5pdCA9IDE1CgogIGRlZiBfX3N0cl9fKHNlbGYpIC0+IHN0cjoKICAgIGlmIHNlbGYuaXNfYWxpdmUoKToKICAgICAgcyA9ICJhbGl2ZSIKICAgIGVsc2U6CiAgICAgIHMgPSAiZGVhZCIKICAgIHJldHVybiBmIiIiRm94OgogIHBvc2l0aW9uOiB7c2VsZi5wYXRjaCgpLmNvb3JkaW5hdGVzKCl9CiAgYWdlOiAgICAgIHtzZWxmLmFnZSgpfQogIGVuZXJneTogICB7c2VsZi5lbmVyZ3koKX0KICBzdGF0dXM6ICAge3N9CiIiIgoKY2xhc3MgUmFiYml0KEFuaW1hbCk6CiAgIiIiCiAgQSByYWJiaXQgaW4gdGhlIHNpbXVsYXRlZCB3b3JsZC4KICAiIiIKCiAgX19zbG90c19fID0gWwogICAgIl81IgogIF0KCiAgZGVmIF9faW5pdF9fKHNlbGYsIHBvcHVsYXRpb24gOiBwYXJhbWV0ZXJzLlBvcHVsYXRpb24sIAogICAgICAgICAgICAgICBwYXRjaCA6IFBhdGNoLCBhZ2UgOiBpbnQpOiAgIAogICAgIiIiCiAgICAgKiBgcG9wdWxhdGlvbmA6IHRoZSBwYXJhbWV0ZXJzIGZvciB0aGUgcmFiYml0IHBvcHVsYXRpb24gdXNlZCBpbiB0aGlzIHJ1biBvZiB0aGUgc2ltdWxhdGlvbi4KICAgICAqIGBwYXRjaGA6IHRoZSBwb3NpdGlvbiBhc3NpZ25lZCB0byB0aGlzIGFuaW1hbCAodGhlIGNvbnN0cnVjdG9yIHRha2VzIGNhcmUgb2YgYWRkaW5nIGl0IHRvIHRoZSBsaXN0IG9mIGFuaW1hbHMgb2YgdGhpcyBwYXRjaCkuCiAgICAgKiBgYWdlYDogdGhlIGN1cnJlbnQgYWdlIG9mIHRoZSBhbmltYWwuCiAgICAiIiIKICAgIGVuZXJneSA9IHJvdW5kKHBvcHVsYXRpb24ubWF4X2VuZXJneSAqIDAuMjUpCiAgICBzZWxmLl81ID0gRmFsc2UKICAgIHN1cGVyKCkuX19pbml0X18ocG9wdWxhdGlvbixwYXRjaCxlbmVyZ3ksYWdlKQogICAgZGVmIGYocyk6CiAgICAgIGlmIHMuaXNfYWxpdmUoKToKICAgICAgICBkID0gcy5fMS5tYXhfZW5lcmd5IC0gcy5fMgogICAgICAgIG0gPSBzLl8wWzBdKDU4Nykocy5fMS5tZXRhYm9saXNtICogUmFiYml0LmZlZWRpbmdfbWV0YWJvbGlzbV9yYXRlKQogICAgICAgIHggPSBtaW4ocy5fNC5ncmFzcygpLCBtLCBkICkKICAgICAgICBpZiB4OgogICAgICAgICAgcy5fNC5fMSAtPSB4CiAgICAgICAgICBzLl8yICs9IHgKICAgIHNlbGYuXzAuYXBwZW5kKGYpCiAgICBzZWxmLl80LmFkZChzZWxmKQoKICBkZWYgaXNfYWxpdmUoc2VsZikgLT4gYm9vbDoKICAgIHJldHVybiBub3Qgc2VsZi5fNSBhbmQgc3VwZXIoKS5pc19hbGl2ZSgpCgogIGRlZiB3YXNfa2lsbGVkKHNlbGYpIC0+IGJvb2w6CiAgICAiIiIKICAgIFRydWUgaWYgdGhlIHJhYmJpdCB3YXMga2lsbGVkIChzZWUgbWV0aG9kIGBraWxsYCkuCiAgICAiIiIKICAgIHJldHVybiBzZWxmLl81CgogIGRlZiBraWxsKHNlbGYpOgogICAgIiIiCiAgICBJZiB0aGUgcmFiYml0IGlzIGFsaXZlLCBpdCBraWxscyBpdCBhbmQgcmVtb3ZlcyBpdCBmcm9tIGl0cyBwYXRjaC4KICAgICIiIgogICAgc2VsZi5fNSA9IFRydWUKICAgIHNlbGYuXzQucmVtb3ZlKHNlbGYpCgogIGRlZiBzYW1lX3NwZWNpZXNfaW4oc2VsZiwgcGF0Y2ggOiBQYXRjaCkgLT4gYm9vbDogICAgCiAgICByZXR1cm4gcGF0Y2guXzBbMF0oMjUzKSgpCgogIGRlZiBwcmVkYXRvcnNfaW4oc2VsZiwgcGF0Y2ggOiBQYXRjaCkgLT4gYm9vbDoKICAgIHJldHVybiBwYXRjaC5fMFsxM10oMjkxKSgpCgogIHJlcHJvZHVjdGlvbl9jb3N0X3JhdGUgPSAwLjkKCiAgZGVmIHJlcHJvZHVjZShzZWxmLCBuZXdib3JuX3BhdGNoKToKICAgIHJldHVybiBzZWxmLl9yZXByb2R1Y2UoUmFiYml0LG5ld2Jvcm5fcGF0Y2gpCiAgCiAgZmVlZGluZ19tZXRhYm9saXNtX3JhdGUgPSAyLjUKCiAgZGVmIF9fc3RyX18oc2VsZikgLT4gc3RyOgogICAgaWYgc2VsZi5pc19hbGl2ZSgpOgogICAgICBzID0gImFsaXZlIgogICAgZWxpZiBzZWxmLndhc19raWxsZWQoKToKICAgICAgcyA9ICJraWxsZWQiCiAgICBlbHNlOgogICAgICBzID0gImRlYWQiCiAgICByZXR1cm4gZiIiIlJhYmJpdDoKICBwb3NpdGlvbjoge3NlbGYucGF0Y2goKS5jb29yZGluYXRlcygpfQogIGFnZTogICAgICB7c2VsZi5hZ2UoKX0KICBlbmVyZ3k6ICAge3NlbGYuZW5lcmd5KCl9CiAgc3RhdHVzOiAgIHtzfQoiIiIK'),'<string>','exec'))