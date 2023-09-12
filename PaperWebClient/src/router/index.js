import { createRouter, createWebHistory } from "vue-router";
// import PresentationView from "../views/Presentation/PresentationView.vue";
// import AboutView from "../views/LandingPages/AboutUs/NotFound.vue";
// import ContactView from "../views/LandingPages/ContactUs/ContactView.vue";
// import AuthorView from "../views/LandingPages/Author/AuthorView.vue";
// import SignInBasicView from "../views/LandingPages/SignIn/BasicView.vue";
// import PageHeaders from "../layouts/sections/page-sections/page-headers/HeadersView.vue";
// import PageFeatures from "../layouts/sections/page-sections/features/FeaturesView.vue";
// import NavigationNavbars from "../layouts/sections/navigation/navbars/NavbarsView.vue";
// import NavigationNavTabs from "../layouts/sections/navigation/nav-tabs/NavTabsView.vue";
// import NavigationPagination from "../layouts/sections/navigation/pagination/PaginationView.vue";
// import InputAreasInputs from "../layouts/sections/input-areas/inputs/InputsView.vue";
// import InputAreasForms from "../layouts/sections/input-areas/forms/FormsView.vue";
// import ACAlerts from "../layouts/sections/attention-catchers/alerts/AlertsView.vue";
// import ACModals from "../layouts/sections/attention-catchers/modals/ModalsView.vue";
// import ACTooltipsPopovers from "../layouts/sections/attention-catchers/tooltips-popovers/TooltipsPopoversView.vue";
// import ElAvatars from "../layouts/sections/elements/avatars/AvatarsView.vue";
// import ElBadges from "../layouts/sections/elements/badges/BadgesView.vue";
// import ElBreadcrumbs from "../layouts/sections/elements/breadcrumbs/BreadcrumbsView.vue";
// import ElButtons from "../layouts/sections/elements/buttons/ButtonsView.vue";
// import ElButtonGroups from "../layouts/sections/elements/button-groups/ButtonGroupsView.vue";
// import ElDropdowns from "../layouts/sections/elements/dropdowns/DropdownsView.vue";
// import ElProgressBars from "../layouts/sections/elements/progress-bars/ProgressBarsView.vue";
// import ElToggles from "../layouts/sections/elements/toggles/TogglesView.vue";
// import ElTypography from "../layouts/sections/elements/typography/TypographyView.vue";

import GetPaper from "@/views/Paper/GetPaper.vue";
import ContactUs from "@/views/Paper/ConnectUs/ContactUs.vue";
import ShowPaper from "@/views/Paper/ShowPaper/ShowPaper.vue";
import DetailPaper from "@/views/Paper/DetailPaper/DetailPaper.vue";
import NotFound from "@/views/Paper/NotFound/NotFound.vue";
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "index",
      component: GetPaper,
    },
    {
      path: "/get_paper",
      name: "get_paper",
      component: GetPaper,
    },
    {
      path: "/show_paper",
      name: "show_paper",
      component: ShowPaper,
    },
    {
      path: "/detail_paper",
      name: "detail_paper",
      component: DetailPaper,
    },
    {
      path: "/contact_us",
      name: "contact_us",
      component: ContactUs,
    },
    {
      path: "/404",
      name: "not_found",
      component: NotFound,
      hidden: true
    },
    {
      path: "/:pathMath(.*)",
      redirect: "/404",
      name: "no_match",
      hidden: true
    },
  ],
});

export default router;
