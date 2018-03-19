<template>
	<div id="main">
		<app-nav></app-nav>
		<transition name="fade" mode="out-in">
			<router-view></router-view>
		</transition>
	</div>
</template>

<script>
import { mapState } from 'vuex';

import AppNav from './components/AppNav.vue';

export default {
	components: {
		AppNav
	},
	computed: {
		...mapState(['loggedIn'])
	},
	watch: {
		loggedIn(loggedIn) {
			if (!loggedIn && this.$route.meta.requiresLogin) {
				this.$router.push({ name: 'login' })
			}
		}
	}
}
</script>

<style lang="scss" scoped>
	.fade-enter-active, .fade-leave-active {
		transition: opacity 300ms ease-in-out;
	}

	.fade-enter, .fade-leave-to {
		opacity: 0;
	}
</style>

