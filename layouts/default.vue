<template>
  <div>
    <info />
    <top />
    <nuxt />
    <bottom />
  </div>
</template>
<script>
import top from '~/components/top.vue'
import bottom from '~/components/bottom.vue'
import info from '~/components/info.vue'

export default {
  components: {
    top,
    bottom,
    info,
  }
}
</script>
